from fastapi import APIRouter, Depends

from modules.auth.schemas import (
    RegisterRequest,
    LoginRequest
)

from modules.auth.service import AuthService
from modules.auth.dependencies import get_current_user

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)


@router.post("/register")
def register(data: RegisterRequest):
    return AuthService.register(data)


@router.post("/login")
def login(data: LoginRequest):
    return AuthService.login(data)


@router.get("/me")
def me(user=Depends(get_current_user)):
    return {
        "authenticated_user": user
    }