from datetime import datetime
from typing import Optional
from pydantic import BaseModel, EmailStr

class UserBase(BaseModel):
    username: str
    firstname: str
    lastname: Optional[str]
    email: EmailStr
    is_superuser: bool = False
    is_active: bool = True
    date_joined: datetime
    
    
class UserCreate(UserBase):
    username: str
    password: str
    
class UserUpdate(UserBase):
    ...

class UserInDBBase(UserBase):
    id: Optional[int] = None
    
    class Config:
        orm_mode = True
        
class UserInDB(UserInDBBase):
    hashed_password: str
    
class User(UserInDBBase):
    ...