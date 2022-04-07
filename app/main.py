import uvicorn
from fastapi import FastAPI

from api.v1 import route
from core.config import settings
from database.base_class import Base
from database.session import engine

Base.metadata.create_all(bind=engine)

app = FastAPI(title=settings.PROJECT_NAME)
app.include_router(route.api_router, prefix=settings.API_V1_STR)

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
