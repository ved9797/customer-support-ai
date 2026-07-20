import os

from dotenv import load_dotenv

from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware

from routes.chat import router

from routes.auth import router as auth_router

from models.chat_models import ChatRequest
from services.chat_service import process_chat

from memory.chat_memory import get_history

from dependencies.auth import get_current_user


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "https://customer-support-ai-d4u9.vercel.app",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)
app.include_router(auth_router)

load_dotenv("../.env")


@app.get("/")
def home():
    return {
        "message": "Hello Vedanshi, your backend is working!"
    }


@app.get("/about")
def about():
    return {
        "project": "Multi-Agent AI Customer Support Assistant",
        "developer": "Vedanshi",
        "version": "2.0",
        "status": "Production Architecture"
    }

@app.post("/chat")
def chat(request: ChatRequest):
    return process_chat(request, None)


@app.get("/memory")
def memory(
    current_user=Depends(get_current_user)
):

    return {
        "chat_history": get_history(
            current_user["user_id"]
        )
    }