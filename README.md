# Customer Support Chatbot with Contextual AI Responses

![Screenshot (613)](https://github.com/user-attachments/assets/987362a2-6d06-4bd1-9e27-3537e9c7d61d)

---

## Overview

An AI-powered chatbot that enhances customer support by delivering context-aware responses. 
Built with FastAPI, Rasa, and React, it integrates AWS DynamoDB for scalable data management, session management and also uses OpenAI ChatGPT for detailed responses. 
Dockerized and deployed on AWS EKS using Kubernetes, 
with a CI/CD pipeline via GitHub Actions for seamless automation.

## Table of Contents

- [Key Features](#key-features)
- [Tech Stack](#tech-stack)
- [Installation](#installation--deployment)
- [Deployment](#deploy-to-aws-eks--github-actions)
- [How project works (Detailed)](#how-this-project-works)
- [Why Built](#why-this-is-built)
- [Screenshots](#screenshots)

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
- DevOps: Docker, Kubernetes (EKS), GitHub Actions, eksctl

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
- Use eksctl to create kubernetes clusters and automatically provision VPCs, subnets, worker nodes and node groups.

## How this project works

> **Rasa** is a conversational AI framework for enterprises that natively leverages generative AI for effortless assistant development. The Rasa model can be fine-tuned according to the developer's preference. Rasa consists of two servers: one is the Rasa server that the chatbot is run on, and the other is the custom actions server that we can create custom actions for. This server is mainly used to connect with other APIs other than the conversation, e.g., like accessing the DynamoDB database to retrieve certain data.

> The **FastAPI** server acts as a bridge between Rasa and external services (e.g., DynamoDB, OpenAI ChatGPT, React frontend) and also provides a high-performance, asynchronous API for handling chatbot requests.

> **DynamoDB** is a NoSQL database optimized for high-speed and low-latency operations. This makes it easier to store user sessions, chat history, and contextual data for better conversation flow.

> Next, **OpenAI ChatGPT** helps increase the chatbot response quality by giving insights about the products to the user.

## Why This is Built

This sample project is built to widen my understanding of pre-trained NLU and NLP models, how they are trained, how they are implemented in production, and also how they are deployed in a cloud-based environment using DevOps.

## Screenshots

Dynamodb database tables

![Screenshot 2025-03-16 200848](https://github.com/user-attachments/assets/98604ca9-b9c3-4333-974f-b0b5c8d40464)

Amazon ECR

![Screenshot 2025-03-16 195958](https://github.com/user-attachments/assets/6c3c7e7c-d9fc-4bc2-8891-81f2e762b3aa)
