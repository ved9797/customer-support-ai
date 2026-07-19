# Changelog

All notable changes to this project will be documented in this file.

This project follows semantic versioning.

---

# [v2.0.0] - Authentication & Backend Refactoring

## ✨ Added

- User registration using FastAPI
- Secure password hashing with bcrypt
- User login
- JWT-based authentication
- Protected `/chat` endpoint
- Authentication routes
- JWT verification dependency
- User collection in MongoDB
- Modular authentication service

## 🚀 Improved

- Refactored backend into a service-oriented architecture
- Simplified `main.py`
- Shared RAG retrieval across AI agents
- Improved conversation memory handling
- Better separation of concerns

## 📂 Project Structure

Added:

- `database/`
- `dependencies/`
- `models/`
- `routes/`
- `services/`
- `tickets/`

---

# Upcoming (v2.1)

- User-specific chat history
- User-specific ticket management
- React authentication
- Protected frontend routes
- Dashboard