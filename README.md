# 🤖 TechMart AI Customer Support Assistant

An AI-powered Multi-Agent Customer Support System built using **FastAPI**, **React**, **Google Gemini**, and a **Retrieval-Augmented Generation (RAG)** pipeline.

The chatbot intelligently routes customer queries to different support agents and retrieves relevant company knowledge before generating responses.

---

# 🚀 Features

- Multi-Agent Architecture
- Billing Support Agent
- Product Support Agent
- Technical Support Agent
- Complaint Resolution Agent
- FAQ Agent
- Knowledge Base using Markdown
- Retrieval-Augmented Generation (RAG)
- React Chat Interface
- FastAPI Backend
- Google Gemini Integration
- Chat Memory
- Auto Scroll
- AI Typing Indicator

---

# 🏗️ Project Architecture

```
                User
                  │
                  ▼
          React Frontend
                  │
                  ▼
          FastAPI Backend
                  │
                  ▼
        Department Router
                  │
     ┌────────────┼────────────┐
     ▼            ▼            ▼
 Billing      Technical     Product
     ▼            ▼            ▼
 Complaint       FAQ
                  │
                  ▼
          Knowledge Base
                  │
                  ▼
        Retrieval (Simple RAG)
                  │
                  ▼
          Google Gemini
                  │
                  ▼
             AI Response
```

---

# 📂 Project Structure

```
customer-support-ai/

├── backend/
│   ├── agents/
│   ├── memory/
│   ├── rag/
│   ├── routes/
│   ├── main.py
│   └── requirements.txt
│
├── frontend/
│   ├── src/
│   ├── public/
│   ├── package.json
│   └── vite.config.js
│
├── knowledge_base/
│
├── datasets/
│
└── README.md
```

---

# 🛠️ Technologies Used

## Backend

- Python
- FastAPI
- Google Gemini API

## Frontend

- React
- Vite
- JavaScript
- CSS

## AI

- Google Gemini 2.5 Flash
- Retrieval-Augmented Generation (RAG)

---

# 📚 Knowledge Base

The chatbot retrieves information from Markdown files such as:

- CompanyProfile.md
- RefundPolicy.md
- Pricing.md
- FAQ.md
- UserManual.md
- ComplaintPolicy.md
- BusinessRules.md

---

# ▶️ Running the Project

## Backend

```bash
cd backend

source venv/bin/activate

uvicorn main:app --reload
```

Backend runs on:

```
http://127.0.0.1:8000
```

---

## Frontend

```bash
cd frontend

npm install

npm run dev
```

Frontend runs on:

```
http://localhost:5173
```

---

# 🔮 Future Improvements

- Vector Database (FAISS)
- Semantic Search
- Authentication
- Database Integration
- Conversation History Storage
- Admin Dashboard

---

# 👩‍💻 Developer

**Vedanshi Chaudhary**

Project developed as part of an AI Customer Support Assistant internship project.
