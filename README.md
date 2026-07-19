# 🛒 TechMart Multi-Agent AI Customer Support Platform

An AI-powered customer support platform built using **React**, **FastAPI**, **Google Gemini**, **MongoDB Atlas**, and **Retrieval-Augmented Generation (RAG)**.

The platform intelligently routes customer queries to specialized AI agents, retrieves relevant information from a knowledge base, maintains conversation history, generates support tickets, and secures user access using JWT authentication.

---

# 🚀 Features

### 🤖 Multi-Agent AI System

The application uses multiple specialized AI agents to handle different customer queries:

- 📦 Product Information Agent
- 💳 Billing Agent
- 🛠 Technical Support Agent
- ❓ FAQ Agent
- ⚠ Complaint Agent

A central **Router Agent** automatically determines which specialized agent should answer each customer query.

---

### 🧠 Retrieval-Augmented Generation (RAG)

Instead of relying only on the LLM's knowledge, the system retrieves relevant company information from a knowledge base before generating responses.

Features include:

- Document Chunking
- Sentence Transformer Embeddings
- Vector Search
- Context Injection into Gemini

---

### 💬 Conversation Memory

The chatbot remembers previous conversations within a session, allowing more natural and contextual interactions.

---

### 🎫 Ticket Generation

If an issue cannot be resolved automatically, the system:

- Creates a support ticket
- Stores it in MongoDB
- Enables smooth human escalation

---

### 🔐 User Authentication

Secure authentication using JWT.

Features:

- User Registration
- User Login
- Password Hashing using bcrypt
- JWT Token Generation
- Protected API Endpoints

---

### 💾 MongoDB Integration

The application stores:

- Registered Users
- Chat History
- Support Tickets

using MongoDB Atlas.

---

# 🏗 System Architecture

```
                    React Frontend
                           │
                           ▼
                  FastAPI Backend
                           │
        ┌──────────────────┼──────────────────┐
        │                  │                  │
        ▼                  ▼                  ▼
 Authentication      Chat Service      Ticket Service
        │                  │
        ▼                  ▼
    JWT Service      Router Agent
                           │
      ┌────────────────────┼────────────────────┐
      ▼                    ▼                    ▼
 Product Agent      Billing Agent      Technical Agent
      │                    │                    │
      └──────────────┬──────────────────────────┘
                     ▼
              Shared RAG Retrieval
                     │
                     ▼
             Google Gemini API
                     │
                     ▼
              MongoDB Atlas
```

---

# 🛠 Tech Stack

## Frontend

- React
- Vite
- JavaScript

## Backend

- FastAPI
- Python
- Pydantic

## Database

- MongoDB Atlas
- PyMongo

## AI

- Google Gemini
- Sentence Transformers
- FAISS

## Authentication

- JWT
- Passlib (bcrypt)

## Other Libraries

- python-dotenv
- email-validator

---

# 📁 Project Structure

```
customer-support-ai/

├── backend/
│
├── agents/
│   ├── billing_agent.py
│   ├── complaint_agent.py
│   ├── faq_agent.py
│   ├── product_agent.py
│   ├── technical_agent.py
│   └── router.py
│
├── database/
│   ├── mongodb.py
│   └── user_db.py
│
├── dependencies/
│   └── auth.py
│
├── memory/
│   └── chat_memory.py
│
├── models/
│   └── auth_models.py
│
├── rag/
│   ├── embeddings.py
│   ├── knowledge_base.py
│   ├── retriever.py
│   ├── text_splitter.py
│   └── vector_store.py
│
├── routes/
│   └── auth.py
│
├── services/
│   ├── ai_service.py
│   ├── auth_service.py
│   ├── chat_service.py
│   └── jwt_service.py
│
├── tickets/
│
├── main.py
│
├── frontend/
│
└── README.md
```

---

# 🔄 Authentication Flow

```
User Registration
        │
        ▼
Password Hashing (bcrypt)
        │
        ▼
MongoDB
        │
        ▼
User Login
        │
        ▼
JWT Token
        │
        ▼
Protected API Endpoints
```

---

# 📚 API Endpoints

| Method | Endpoint | Description |
|---------|----------|-------------|
| POST | `/register` | Register a new user |
| POST | `/login` | Login user |
| POST | `/chat` | Chat with AI (JWT Protected) |

---

# 🗄 Database Collections

MongoDB stores:

```
users
chat_history
tickets
```

---

# ⚙ Installation

## Clone Repository

```bash
git clone https://github.com/<your-username>/customer-support-ai.git

cd customer-support-ai
```

---

## Backend Setup

```bash
cd backend

python -m venv venv

source venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run backend

```bash
uvicorn main:app --reload
```

---

## Frontend Setup

```bash
cd frontend

npm install

npm run dev
```

---

# 🔑 Environment Variables

Create a `.env` file inside the backend directory.

Example:

```env
MONGODB_URI=your_mongodb_connection_string

GEMINI_API_KEY=your_gemini_api_key

JWT_SECRET_KEY=your_secret_key

JWT_ALGORITHM=HS256

JWT_EXPIRE_MINUTES=60
```

---

# 📌 Future Enhancements

- User-specific chat history
- User-specific support tickets
- Admin Dashboard
- Chat Analytics
- Role-Based Access Control (RBAC)
- Docker Support
- CI/CD Pipeline
- Unit & Integration Testing
- Cloud Deployment (AWS/Azure/GCP)

---

# 📖 Learning Objectives

This project demonstrates:

- FastAPI Backend Development
- REST API Design
- JWT Authentication
- Retrieval-Augmented Generation (RAG)
- Multi-Agent AI Architecture
- MongoDB Integration
- React Frontend Development
- AI-powered Customer Support Systems
- Software Architecture & Modular Design

---

# 👩‍💻 Author

**Vedanshi Chaudhary**

If you found this project interesting, feel free to ⭐ the repository.