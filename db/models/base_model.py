from sqlalchemy import Column, String
import uuid

from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# class_registry: t.Dict = {}


# @as_declarative(class_registry=class_registry)
class BaseModel(Base):
    __abstract__ = True
    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))

