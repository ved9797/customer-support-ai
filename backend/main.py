import os
from dotenv import load_dotenv

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from pydantic import BaseModel
from google import genai

from routes.chat import router

# Router
from agents.router import detect_department

# Agents
from agents.billing_agent import billing_prompt
from agents.technical_agent import technical_prompt
from agents.product_agent import product_prompt
from agents.complaint_agent import complaint_prompt
from agents.faq_agent import faq_prompt

# Memory
from memory.chat_memory import add_message, get_history

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)

load_dotenv("../.env")
client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


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
        "status": "Learning FastAPI"
    }


class ChatRequest(BaseModel):
    message: str


@app.post("/chat")
def chat(request: ChatRequest):

    # Detect which department should handle the query
    department = detect_department(request.message)

    print(f"Department: {department}")

    # Select the correct AI Agent
    if department == "Billing":
        prompt = billing_prompt(request.message)

    elif department == "Technical":
        prompt = technical_prompt(request.message)

    elif department == "Product":
        prompt = product_prompt(request.message)

    elif department == "Complaint":
        prompt = complaint_prompt(request.message)

    elif department == "FAQ":
        prompt = faq_prompt(request.message)

    else:
        prompt = request.message

    # Save user's message
    add_message("user", request.message)

    try:
        # Send prompt to Gemini
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        ai_reply = response.text

    except Exception as e:
        print("Gemini Error:", e)
        ai_reply = "Gemini is currently busy. Please try again in a moment."

    # Save AI response
    add_message("assistant", ai_reply)

    print(get_history())

    return {
        "department": department,
        "your_message": request.message,
        "ai_response": ai_reply
    }


@app.get("/memory")
def memory():
    return {
        "chat_history": get_history()
    }