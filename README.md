🧠Two-Tier Flask App with MySQL & Jenkins CI/CD
---
📋 Overview
This project demonstrates the deployment of a Flask web application with a MySQL database using Docker & Docker Compose, along with a CI/CD pipeline built in Jenkins.
It’s a complete beginner-to-intermediate level DevOps project that covers local development, containerization, vulnerability scanning, and continuous deployment.

---
🛠️ Tools & Technologies Used
<p align="center"> <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white"/> <img src="https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white"/> <img src="https://img.shields.io/badge/MySQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white"/> <img src="https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white"/> <img src="https://img.shields.io/badge/Docker%20Compose-384d54?style=for-the-badge&logo=docker&logoColor=white"/> <img src="https://img.shields.io/badge/Jenkins-D24939?style=for-the-badge&logo=jenkins&logoColor=white"/> <img src="https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white"/> <img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white"/> <img src="https://img.shields.io/badge/Docker%20Scout-0db7ed?style=for-the-badge&logo=docker&logoColor=white"/> <img src="https://img.shields.io/badge/Kali%20Linux-557C94?style=for-the-badge&logo=kalilinux&logoColor=white"/> </p>

---
⚙️ Project Architecture
Two-tier architecture:
Tier 1 (Web App): Flask container
Tier 2 (Database): MySQL container
Communication between containers is managed via Docker network using docker-compose.yml.

---

🚀 Step-by-Step Implementation

🟡Step 1: Clone the Repository
git clone https://github.com/Eman-gul457/two-tier-flask-app.git
cd two-tier-flask-app
<img width="653" height="198" alt="git-clone" src="https://github.com/user-attachments/assets/c97910b4-bc5f-40c0-8466-7bfe5c802488" />

---

🟡Step 2: Verify Files
ls -R
<img width="332" height="253" alt="app-structure" src="https://github.com/user-attachments/assets/d9c4d021-d0c0-48a8-a5de-8162c6d39b6a" />

---

🟡Step 3: Build Docker Image
docker build -t flask-app:latest 
<img width="1336" height="341" alt="docker-build" src="https://github.com/user-attachments/assets/06ef6dcd-c27f-4c49-9227-38df8e01cd7c" />

---

🟡Step 4: Run Containers
docker-compose up -d

---

🟡Step 5: Verify Running Containers
docker ps
<img width="1246" height="94" alt="docker-ps" src="https://github.com/user-attachments/assets/1478d576-1e26-4478-9e42-4684edb4c71b" />

---

🟡Step 7: Open Application
Visit in browser:
👉 http://localhost:5000
<img width="1325" height="519" alt="app-running" src="https://github.com/user-attachments/assets/936ba9dc-52f9-422f-b21d-4716d2d40e49" />

---

🟡Step 8: Scan for Vulnerabilities
docker scout cves flask-app:latest
<img width="605" height="287" alt="docker-scout" src="https://github.com/user-attachments/assets/d5b8ce7e-fd0f-412e-a6d1-b52446636c2b" />

---

🟡Step 10: Push Image to DockerHub
docker tag flask-app eman-gul457/two-tier-flask-app:latest
docker login
docker push eman-gul457/two-tier-flask-app:latest
<img width="906" height="276" alt="dockerhub-repo" src="https://github.com/user-attachments/assets/96a94b59-0548-4342-af7f-1d25d71891ff" />

---

🟡Step 11: Setup Jenkins CI/CD
🔹Install Jenkins & Docker plugins
🔹Configure Jenkins credentials for GitHub and DockerHub
🔹Create a new pipeline project
🔹Use the Jenkinsfile
<img width="1356" height="466" alt="jenkins-pipeline" src="https://github.com/user-attachments/assets/2c0d60a0-466a-4aba-9a27-a7faa78a24ac" />
<img width="770" height="300" alt="jenkins-dashboard" src="https://github.com/user-attachments/assets/81e6f5be-f6e2-4ddb-be73-2464be58d60b" />

---

📊 Project Flow Summary
1.Developer pushes code → GitHub
2.Jenkins pulls the latest commit
3.Jenkins builds Docker image
4.Image scanned for vulnerabilities
5.If clean, pushed to DockerHub automatically
6.Flask app can be deployed from DockerHub on any host

---

🏁 Conclusion
This project demonstrates an end-to-end DevOps workflow — from local app development, containerization, image security scanning, to automated CI/CD deployment.
It’s a solid addition to your DevOps portfolio.

---


