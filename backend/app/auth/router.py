from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.auth.schema import LoginRequest
from app.auth.service import authenticate_user
from app.auth.security import create_access_token

from app.database.session import get_db
from app.auth.schema import RegisterRequest
from app.auth.service import create_user
from app.auth.dependencies import get_current_user
from app.models.user import User

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)

@router.post("/register")
def register(
    request: RegisterRequest,
    db: Session = Depends(get_db)
):
    user = create_user(
        db=db,
        name=request.name,
        email=request.email,
        phone=request.phone,
        password=request.password,
    )
    if not user:
        raise HTTPException(
            status_code=400,
            detail="Email already exists"
        )
    
    return {
        "message": "User registered successfully"
    }

@router.post("/login")
def login(
    request: LoginRequest,
    db: Session = Depends(get_db)
):
    user = authenticate_user(
        db,
        request.email,
        request.password
    )

    if not user:
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password"
        )
    token = create_access_token(
        {
            "sub": str(user.id),
            "email": user.email
        }
    )

    return {
        "access_token": token,
        "token_type": "bearer"
    }

@router.get("/me")
def get_me(current_user: User = Depends(get_current_user)):
    return {
        "id": current_user.id,
        "name": current_user.name,
        "email": current_user.email,
        "phone": current_user.phone,
    }