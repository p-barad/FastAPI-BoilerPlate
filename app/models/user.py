from datetime import datetime
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship

from database.base_class import Base

class User(Base):
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, index=True, nullable=False)
    firstname = Column(String(50), nullable=False)
    lastname = Column(String(50), nullable=True)
    email = Column(String(50), unique=True, nullable=False, index=True)
    is_superuser = Column(Boolean, default=False)
    hashed_password = Column(String(256))
    is_active = Column(Boolean, default=True)
    date_joined = Column(DateTime, default=datetime.utcnow())