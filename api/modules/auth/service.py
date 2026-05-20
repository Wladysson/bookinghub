from modules.auth.repository import AuthRepository
from modules.auth.password import (
    hash_password,
    verify_password
)
from modules.auth.jwt_handler import create_access_token
from fastapi import HTTPException


class AuthService:

    @staticmethod
    def register(data):
        existing_user = AuthRepository.find_by_email(
            data.email
        )

        if existing_user:
            raise HTTPException(
                status_code=400,
                detail="Email already registered"
            )

        hashed = hash_password(data.password)

        user = AuthRepository.create_user(
            name=data.name,
            email=data.email,
            hashed_password=hashed
        )

        return {
            "id": user[0],
            "name": user[1],
            "email": user[2]
        }

    @staticmethod
    def login(data):
        user = AuthRepository.find_by_email(
            data.email
        )

        if not user:
            raise HTTPException(
                status_code=401,
                detail="Invalid credentials"
            )

        valid_password = verify_password(
            data.password,
            user[3]
        )

        if not valid_password:
            raise HTTPException(
                status_code=401,
                detail="Invalid credentials"
            )

        token = create_access_token({
            "sub": str(user[0]),
            "email": user[2]
        })

        return {
            "access_token": token,
            "token_type": "bearer"
        }