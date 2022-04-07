from sqlalchemy.ext.declarative import as_declarative, declared_attr #, declarative_base
from typing import Any

@as_declarative()
class Base:
    id: Any
    __name__: str
    
    # Generate __tablename__ automatically
    @declared_attr
    def __tablename__(self) -> str:
        return self.__name__.lower()

# Base = declarative_base()