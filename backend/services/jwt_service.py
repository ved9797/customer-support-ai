import os

import jwt
from dotenv import load_dotenv
from fastapi import HTTPException, status

load_dotenv("../.env")

JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")
JWT_ALGORITHM = os.getenv("JWT_ALGORITHM")


def verify_token(token: str):

    print("==============")
    print("TOKEN RECEIVED:")
    print(token)
    print("SECRET:", JWT_SECRET_KEY)
    print("ALGORITHM:", JWT_ALGORITHM)
    print("==============")

    try:
        payload = jwt.decode(
            token,
            JWT_SECRET_KEY,
            algorithms=[JWT_ALGORITHM]
        )

        print("Decoded:", payload)

        return payload

    except Exception as e:
        print("JWT ERROR:", repr(e))

        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=str(e)
        )