from sqlalchemy import Column, String, DECIMAL, Text, ForeignKey, DateTime, Boolean
from sqlalchemy.orm import relationship

from db.models.base_model import BaseModel
# from db.models.user import User # noqa


class Spending(BaseModel):
    __tablename__ = 'spendings'

    recipient = Column(String(255), nullable=False)
    amount = Column(DECIMAL(10, 2), nullable=False)
    currency = Column(String(3), nullable=False)
    spending_type = Column(String(255), nullable=False)
    transaction_time = Column(DateTime, nullable=False)
    is_necessary = Column(Boolean, nullable=False)
    notes = Column(Text)
    user_id = Column(String(36), ForeignKey('users.id'), nullable=False)

    # relationship to User
    user = relationship("User", back_populates="spendings")

    def dict(self):
        return {
            'id': self.id,
            'recipient': self.recipient,
            'amount': self.amount,
            'currency': self.currency,
            'spending_type': self.spending_type,
            'transaction_time': self.transaction_time,
            'is_necessary': self.is_necessary,
            'notes': self.notes,
            'user_id': self.user_id
        }
