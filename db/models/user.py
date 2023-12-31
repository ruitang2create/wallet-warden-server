from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from db.models.base_model import BaseModel
# from db.models.spending import Spending # noqa
# from db.models.income import Income # noqa


class User(BaseModel):
    __tablename__ = 'users'

    username = Column(String(50), unique=True, nullable=False)
    password = Column(String(256), nullable=False)
    password_salt = Column(String(128), nullable=False)
    spendings = relationship("Spending", back_populates="user")
    incomes = relationship("Income", back_populates="user")

    def dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'password': self.password,
            'password_salt': self.password_salt
        }