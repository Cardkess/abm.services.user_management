from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import jwt
from datetime import datetime, timedelta
from app.models.user import User
from app.core.config import settings
from app.db import get_database
import bcrypt

router = APIRouter()

ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

def create_access_token(data: dict, expires_in: int = ACCESS_TOKEN_EXPIRE_MINUTES):
    to_encode = data.copy()
    to_encode["exp"] = datetime.utcnow() + timedelta(minutes=expires_in)
    return jwt.encode(to_encode, settings.SECRET_KEY, algorithm=ALGORITHM)

def get_password_hash(password: str):
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

def verify_password(plain_password, hashed_password):
    return bcrypt.checkpw(plain_password.encode('utf-8'), hashed_password.encode('utf-8'))

@router.post("/token")
async def login(username: str, password: str):
    # Implement login logic here
    pass

@router.post("/users")
async def create_user(username: str, password: str):
    # Implement user creation logic here
    pass

@router.get("/users")
async def get_list_of_all_users():
    db = await get_database()
    user = User(username="Cardkess", password="password", email="bchidambe@gmail.com")
    await user.save()
    pass