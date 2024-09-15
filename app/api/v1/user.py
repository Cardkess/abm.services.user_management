from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import jwt
from datetime import datetime, timedelta
from app.models.user import User
from app.core.config import settings
from app.db import get_database
from app.schemas.user import UserCreate, UserResponse, UserUpdate
from app.core.security import get_password_hash, verify_password, create_access_token
from tortoise.transactions import in_transaction
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

@router.post("/users", response_model=UserResponse)
async def create_user(user: UserCreate):
    async with in_transaction():
        
        # Check if user with the same username or email already exists
        existing_username = await User.filter(username=user.username).first()
        
        if existing_username:
            raise HTTPException(status_code=400, detail="Username already registered")
        
        existing_email = await User.filter(email=user.email).first()
        
        if existing_email:
            raise HTTPException(status_code=400, detail="Email already registered")
        
        
        # Convert the Pydantic model to a dictionary and exclude 'password'
        user_data = user.dict(exclude={"password"})
        
        # Hash the password
        user_data["password"] = get_password_hash(user.password)
        
        # Create the user in the database
        db_user = await User.create(**user_data)
        
    return await UserResponse.from_tortoise_orm(db_user)
   
@router.get("/users")
async def get_list_of_all_users():
    db = await get_database()
    
    pass