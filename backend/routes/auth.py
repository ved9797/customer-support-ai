from fastapi import APIRouter, HTTPException

from models.auth_models import RegisterRequest
from services.auth_service import register_user

from models.auth_models import LoginRequest
from services.auth_service import login_user

router = APIRouter(tags=["Authentication"])


@router.post("/register")
def register(request: RegisterRequest):

    try:
        return register_user(request)

    except ValueError as e:
        raise HTTPException(
            status_code=400,
            detail=str(e)
        )
    
@router.post("/login")
def login(request: LoginRequest):

    try:
        return login_user(request)

    except ValueError as e:
        raise HTTPException(
            status_code=401,
            detail=str(e)
        )