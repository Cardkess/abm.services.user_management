from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import date
from uuid import UUID
from tortoise.contrib.pydantic import pydantic_model_creator
from app.models.user import User

class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str
    first_name: str
    last_name: str
    gender: Optional[str] = None
    phone_number: Optional[str] = None
    address: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    country: Optional[str] = None
    postal_code: Optional[str] = None
    date_of_birth: Optional[date] = None
    preferred_payment_method: Optional[str] = None

class UserUpdate(BaseModel):
    username: Optional[str] = None
    email: Optional[EmailStr] = None
    password: Optional[str] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    gender: Optional[str] = None
    phone_number: Optional[str] = None
    address: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    country: Optional[str] = None
    postal_code: Optional[str] = None
    date_of_birth: Optional[date] = None
    preferred_payment_method: Optional[str] = None

UserResponseBase = pydantic_model_creator(User, name="UserResponse", exclude=("password",))

class UserResponse(UserResponseBase):
    class Config:
        from_attributes = True

class Config:
    from_attributes = True
