from pydantic import BaseModel, UUID4
from typing import List
from datetime import datetime


class SpendingBase(BaseModel):
    recipient: str
    amount: float
    currency: str
    spending_type: str
    transaction_time: datetime
    is_necessary: bool
    notes: str


class CreateSpendingRequestSchema(SpendingBase):
    ...


class CreateSpendingSchema(SpendingBase):
    user_id: UUID4


class SpendingResponseSchema(SpendingBase):
    id: UUID4
    user_id: UUID4

    class Config:
        orm_mode: True


class SpendingListResponseSchema(BaseModel):
    spendings: List[SpendingResponseSchema]