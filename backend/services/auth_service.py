from datetime import datetime

from passlib.context import CryptContext

from database.user_db import user_collection

import os
from datetime import datetime, timedelta, UTC

import jwt
from dotenv import load_dotenv

load_dotenv("../.env")

JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")
JWT_ALGORITHM = os.getenv("JWT_ALGORITHM")
JWT_EXPIRE_MINUTES = int(os.getenv("JWT_EXPIRE_MINUTES", "60"))

pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)


def hash_password(password: str) -> str:
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(
        plain_password,
        hashed_password
    )


def get_user_by_email(email: str):
    return user_collection.find_one({"email": email})


def register_user(request):

    print("Password:", request.password)
    print("Password Length:", len(request.password))

    existing_user = get_user_by_email(request.email)

    if existing_user:
        raise ValueError("Email already registered.")

    user = {
        "name": request.name,
        "email": request.email,
        "password": hash_password(request.password),
        "created_at": datetime.utcnow()
    }

    result = user_collection.insert_one(user)

    return {
        "user_id": str(result.inserted_id),
        "name": request.name,
        "email": request.email
    }

def create_access_token(user):

    payload = {
        "user_id": str(user["_id"]),
        "name": user["name"],
        "email": user["email"],
        "exp": datetime.now(UTC) + timedelta(minutes=JWT_EXPIRE_MINUTES)
    }

    return jwt.encode(
        payload,
        JWT_SECRET_KEY,
        algorithm=JWT_ALGORITHM
    )


def login_user(request):

    user = get_user_by_email(request.email)

    if not user:
        raise ValueError("Invalid email or password.")

    if not verify_password(request.password, user["password"]):
        raise ValueError("Invalid email or password.")

    token = create_access_token(user)

    return {
        "access_token": token,
        "token_type": "bearer",
        "user": {
            "id": str(user["_id"]),
            "name": user["name"],
            "email": user["email"]
        }
    }
