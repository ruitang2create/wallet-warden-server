from sqlalchemy.orm import Session
from fastapi import Depends, APIRouter
from starlette.status import HTTP_201_CREATED

from api.depends import get_db
# from api.server import app
from db.schemas.income import GetIncomeListSchema, GetIncomeSchema, CreateIncomeSchema
from db.crud.crud_income import Income_Manager

router = APIRouter()


@router.get("/", response_model=GetIncomeListSchema)
def fetch_all_incomes(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    records = Income_Manager.get_multi(db=db, skip=skip, limit=limit)
    return {
        "incomes": records,
    }


@router.get("/user", response_model=GetIncomeListSchema)
def fetch_all_incomes_by_user(user_id: str, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    print(f'Select spending records whose user_id = {user_id}')
    records = Income_Manager.get_multi_by_user_id(db=db, user_id=user_id, skip=skip, limit=limit)
    return {
        "incomes": records,
    }


@router.post("/user", response_model=GetIncomeSchema, status_code=HTTP_201_CREATED)
def create_income(payload: CreateIncomeSchema, db: Session = Depends(get_db)):
    record = Income_Manager.create(db=db, obj_in=payload)

    return record


