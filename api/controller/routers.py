from fastapi import APIRouter
from api.controller import auth, income, spending

api_router = APIRouter()
api_router.include_router(income.router, prefix="/incomes", tags=["incomes"])
api_router.include_router(spending.router, prefix="/spendings", tags=["spendings"])
api_router.include_router(auth.router, prefix="/auth", tags=["auth"])
