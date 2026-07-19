import os
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv("../.env")

MONGODB_URI = os.getenv("MONGODB_URI")

print("Mongo URI Loaded:", bool(MONGODB_URI))

client = MongoClient(
    MONGODB_URI,
    serverSelectionTimeoutMS=5000
)

try:
    client.admin.command("ping")
    print("✅ MongoDB Connected Successfully")
except Exception as e:
    print("❌ MongoDB Connection Failed")
    print(e)

db = client["customer_support_ai"]

chat_collection = db["chat_history"]