# 🚀 Dockerized Flask API with PostgreSQL

## 📌 Overview
This project demonstrates a containerized Python Flask API connected to a PostgreSQL database using Docker and Docker Compose.

## 🏗 Architecture
Client → Flask API (Container) → PostgreSQL (Container) → Docker Volume

## ⚙️ Features
- Multi-container setup using Docker Compose
- Persistent storage using Docker volumes
- Environment variable-based configuration
- CI/CD pipeline using GitHub Actions
- Docker image push to Docker Hub

## 🧰 Tech Stack
- Python (Flask)
- PostgreSQL
- Docker
- Docker Compose
- GitHub Actions

## 🚀 How to Run

docker compose up --build

Access:
http://localhost:5000

## 🔄 CI/CD Pipeline
- Trigger: Push to GitHub
- Builds Docker image
- Pushes image to Docker Hub

## 🔮 Future Improvements
- Deploy on AWS EC2
- Add monitoring and logging
