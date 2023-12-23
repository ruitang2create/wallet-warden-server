from sqlalchemy import Column, String, DECIMAL, Text, ForeignKey, DateTime, Boolean
from sqlalchemy.orm import relationship

from db.models.base_model import BaseModel
# from db.models.user import User # noqa


class Income(BaseModel):
    __tablename__ = 'incomes'

    source = Column(String(255), nullable=False)
    amount = Column(DECIMAL(10, 2), nullable=False)
    currency = Column(String(3), nullable=False)
    income_type = Column(String(255), nullable=False)
    transaction_time = Column(DateTime, nullable=False)
    is_regular = Column(Boolean, nullable=False)
    notes = Column(Text)
    user_id = Column(String(36), ForeignKey('users.id'), nullable=False)

    # relationship to User
    user = relationship("User", back_populates="incomes")

    def dict(self):
        return {
            'id': self.id,
            'source': self.source,
            'amount': self.amount,
            'currency': self.currency,
            'income_type': self.income_type,
            'transaction_time': self.transaction_time,
            'notes': self.notes,
            'user_id': self.user_id
        }