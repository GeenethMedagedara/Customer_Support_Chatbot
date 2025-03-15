# Customer Support Chatbot with Contextual AI Responses

![Screenshot (613)](https://github.com/user-attachments/assets/987362a2-6d06-4bd1-9e27-3537e9c7d61d)

---

## Overview

An AI-powered chatbot that enhances customer support by delivering context-aware responses. 
Built with FastAPI, Rasa, and React, it integrates AWS DynamoDB for scalable data management, session management and also uses OpenAI ChatGPT for detailed responses. 
Dockerized and deployed on AWS EKS using Kubernetes, 
with a CI/CD pipeline via GitHub Actions for seamless automation.

## Key Features

- **Context-Aware Responses** – Understands user queries and maintains conversation flow.
- **Multi-Turn Conversations** – Supports dynamic, multi-step interactions.
- **Scalable & Cloud-Hosted** – Deployed on AWS Kubernetes (EKS) with DynamoDB.
- **Real-Time API** – FastAPI backend with async processing for speed and efficiency.
- **Detailed Responses** – Supports responses with included details using ChatGPT.
- **CI/CD Automation** – GitHub Actions pipeline for continuous deployment.

## Tech Stack

- Backend: FastAPI, Python, AWS DynamoDB, OpenAI ChatGPT
- Chatbot: Rasa (NLP, NLU, custom actions)
- Frontend: React, Tailwind CSS
- DevOps: Docker, Kubernetes (EKS), GitHub Actions

## Installation & Deployment

### Run Locally

1. Clone the repository:

```
git clone https://github.com/GeenethMedagedara/Customer_Support_Chatbot.git
cd customer-support-chatbot
```

2. Start the services directly using Docker:

```
docker-compose up --build
```

3. Access the chatbot UI at [http://localhost:5173](http://localhost:5173)

## Deploy to AWS (EKS + GitHub Actions)

- Push Docker images to **AWS ECR**
- Apply Kubernetes configurations (kubectl apply -f k8s/)
- Monitor deployment with kubectl get pods

## Screenshots
