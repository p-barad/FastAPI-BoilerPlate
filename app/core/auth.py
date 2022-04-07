from datetime import datetime, timedelta
from typing import Optional #, MutableMapping, Union

from fastapi.security import OAuth2PasswordBearer
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm.session import Session
from jose import jwt

from models.user import User
from core.config import settings
from core.security import verify_password

# -- WHY?? --
# JWTPayloadMapping = MutableMapping[
#     str, Union[datetime, bool, str, list[str], list[int]]
# ]

oauth2_scheme = OAuth2PasswordBearer(tokenUrl=f"{settings.API_V1_STR}/auth/login")

def authenticate_user(db: Session, username: str, password: str) -> Optional[User]:
    user = db.query(User).filter(User.username == username).first()
    if not user:
        return None
    if not verify_password(password, user.hashed_password):
        return None
    return user 

def create_access_token(*, sub: str) -> str:
    return _create_token(
        token_type="access_token",
        lifetime=timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES),
        sub=sub,
    )

def _create_token(token_type: str, lifetime: timedelta, sub: str) -> str:
    payload = {}
    expire = datetime.utcnow() + lifetime
    
    payload["type"] = token_type
    payload["expire"] = jsonable_encoder(expire)
    payload["sub"] = sub
    
    return jwt.encode(payload, settings.SECRET_KEY, algorithm=settings.ALGORITHM)