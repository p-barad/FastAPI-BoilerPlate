from typing import Any
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

import schemas
from api import deps
from core.auth import authenticate_user, create_access_token
from crud import crud_user
from models.user import User

router = APIRouter()

@router.post("/login")
def login(db: Session = Depends(deps.get_db), form_data: OAuth2PasswordRequestForm = Depends()) -> Any:
    """
    Get the JWT for a user with data from OAuth2 request form body.
    """
    
    user = authenticate_user(db=db, username=form_data.username, password=form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password"
        )
    
    return {
        "access_token": create_access_token(sub=user.username),
        "token_type": "bearer",
    }
    
@router.get("/me", response_model=schemas.user.User)
def read_users_me(current_user: User = Depends(deps.get_current_active_user)):
    """
    Fetch the current logged in user.
    """
    
    return current_user

@router.post("/signup", response_model=schemas.user.User, status_code=status.HTTP_201_CREATED)
def create_user_signup(*, db: Session = Depends(deps.get_db), user_in: schemas.user.UserCreate) -> Any:
    """
    Create new user without the need to be logged in.
    """

    user = db.query(User).filter(User.username == user_in.username).first()
    if user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="The user with this username already exists in thise system"
        )
    
    user = crud_user.user.create(db=db, obj_in=user_in)
    
    return user