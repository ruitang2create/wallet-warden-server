from pydantic import BaseModel, UUID4
from typing import List
from datetime import datetime


class CreateSpendingSchema(BaseModel):
    recipient: str
    amount: float
    currency: str
    spending_type: str
    transaction_time: datetime
    is_necessary: bool
    user_id: UUID4
    notes: str


class GetSpendingSchema(BaseModel):
    id: UUID4
    recipient: str
    amount: float
    currency: str
    spending_type: str
    transaction_time: datetime
    is_necessary: bool
    user_id: UUID4
    notes: str

    class Config:
        orm_mode: True


class GetSpendingListSchema(BaseModel):
    spendings: List[GetSpendingSchema]