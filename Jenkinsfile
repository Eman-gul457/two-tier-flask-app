pipeline {
    agent any

    environment {
        DOCKER_HUB_REPO = 'eman-gul457/two-tier-flask-app'
    }

    stages {
        stage('Checkout SCM') {
            steps {
                checkout scm
            }
        }

        stage('Clone Repository') {
            steps {
                echo 'Cloning repository...'
                sh 'git clone https://github.com/Eman-gul457/two-tier-flask-app.git || true'
            }
        }

        stage('Build Docker Image') {
            steps {
                echo 'Building Docker image...'
                sh 'docker build -t $DOCKER_HUB_REPO:latest .'
            }
        }

        stage('Push to Docker Hub') {
            steps {
                echo 'Pushing image to Docker Hub...'
                withCredentials([string(credentialsId: 'dockerhub-pass', variable: 'DOCKER_HUB_PASS')]) {
                    sh '''
                    echo "$DOCKER_HUB_PASS" | docker login -u eman-gul457 --password-stdin
                    docker push $DOCKER_HUB_REPO:latest
                    '''
                }
            }
        }

        stage('Deploy to Server') {
            steps {
                echo 'Deploying latest Docker image...'
                sh '''
                docker stop flask-app || true
                docker rm flask-app || true
                docker pull $DOCKER_HUB_REPO:latest
                docker run -d -p 5000:5000 --name flask-app $DOCKER_HUB_REPO:latest
                '''
            }
        }
    }

    post {
        always {
            echo 'Cleaning up...'
            sh 'docker system prune -f || true'
        }
    }
}
