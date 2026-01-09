# DevOps Microservice

Production-ready Python Flask microservice with CI/CD pipeline using Jenkins and Docker.

## Endpoints
- / : Home
- /health : Health Check

## Run Locally
pip install -r requirements.txt
python app/main.py

## Docker
docker build -t devops-microservice .
docker run -d -p 5000:5000 devops-microservice
