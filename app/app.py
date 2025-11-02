from flask import Flask, render_template
import mysql.connector

app = Flask(__name__)

@app.route('/')
def home():
    connection = mysql.connector.connect(
        host="db",          # service name in docker-compose.yml
        user="root",
        password="root",
        database="flaskdb"
    )
    cursor = connection.cursor()
    cursor.execute("SELECT 'Hello from MySQL!'")
    result = cursor.fetchone()
    connection.close()
    return render_template('index.html', message=result[0])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
