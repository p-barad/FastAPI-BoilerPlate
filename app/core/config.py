import secrets
from pydantic import AnyHttpUrl, BaseSettings, EmailStr


class Settings(BaseSettings):
    PROJECT_NAME: str = "MyProject"
    
    API_V1_STR: str = "/api/v1"
    SECRET_KEY: str = secrets.token_urlsafe(32)
    ALGORITHM: str = "HS256"
    
    # 60 mins * 24 hrs * 7 days = 7days
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7
    
    BACKEND_CORS_ORIGINS: list[AnyHttpUrl] = [
        "http://localhost",
        "http://127.0.0.1"
    ]
    
    
    SQL_DATABASE_URI: str = (
        "mysql+mysqlconnector://root:ZOOTzxcv*05@localhost:3306/fastapi"
    )
    FIRST_SUPERUSER: EmailStr = "admin@recipeapi.com"
    FIRST_SUPERUSER_PW: str = "CHANGEME"

    class Config:
        case_sensitive = True


settings = Settings()
