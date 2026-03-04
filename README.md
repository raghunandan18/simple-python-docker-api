📦 Simple Python Docker API
🔹 Overview

This project demonstrates how to containerize a Python Flask application using Docker and Docker Compose.
The application exposes basic API endpoints and supports environment-based configuration.

🔹 Tech Stack

Python 3.10

Flask

Docker

Docker Compose

🔹 Features

REST API with / and /health endpoints

Dockerized application

Environment variable configuration

Compose-based service orchestration

🔹 Run Locally
docker build -t simple-python-api .
docker run -p 5000:5000 simple-python-api
🔹 Run with Docker Compose
docker compose up --build
🔹 Access Endpoints
http://localhost:5000
http://localhost:5000/health
🔹 Learning Outcomes

Understanding Docker image layers

Container runtime vs build-time

Port mapping

Environment variable injection

Service orchestration using docker-compose

## Architecture

Client
  ↓
Flask API (Docker Container)
  ↓
PostgreSQL Database (Docker Container)
  ↓
Docker Volume for persistent data

## Run the Project

docker compose up --build
