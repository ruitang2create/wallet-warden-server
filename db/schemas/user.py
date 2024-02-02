from pydantic import BaseModel, UUID4
from typing import List
from datetime import datetime


class CreateIncomeSchema(BaseModel):
    source: str
    amount: float
    currency: str
    income_type: str
    transaction_time: datetime
    is_regular: bool
    user_id: UUID4
    notes: str


class GetIncomeSchema(BaseModel):
    id: UUID4
    source: str
    amount: float
    currency: str
    income_type: str
    transaction_time: datetime
    is_regular: bool
    user_id: UUID4
    notes: str

    class Config:
        orm_mode: True


class GetIncomeListSchema(BaseModel):
    incomes: List[GetIncomeSchema]
