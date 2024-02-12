from sqlalchemy.orm import Session
from fastapi import Depends, APIRouter
from starlette.status import HTTP_201_CREATED

from api.depends import get_db, get_current_user

from db.schemas.income import IncomeListResponseSchema, IncomeResponseSchema, CreateIncomeRequestSchema, \
    CreateIncomeSchema
from db.crud.crud_income import Income_Manager

router = APIRouter()


@router.get("/", response_model=IncomeListResponseSchema)
def fetch_all_incomes(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    records = Income_Manager.get_multi(db=db, skip=skip, limit=limit)
    return {
        "incomes": records,
    }


@router.get("/user", response_model=IncomeListResponseSchema)
def fetch_all_incomes_by_user(skip: int = 0, limit: int = 100, db: Session = Depends(get_db),
                              user=Depends(get_current_user)):
    print(f'Select spending records whose user_id = {user.id}')
    records = Income_Manager.get_multi_by_user_id(db=db, user_id=user.id, skip=skip, limit=limit)
    return {
        "incomes": records,
    }


@router.post("/user", response_model=IncomeResponseSchema, status_code=HTTP_201_CREATED)
def create_income(payload: CreateIncomeRequestSchema, db: Session = Depends(get_db), user=Depends(get_current_user)):
    data_in: CreateIncomeSchema = CreateIncomeSchema(source=payload.source,
                                                     amount=payload.amount,
                                                     currency=payload.currency,
                                                     income_type=payload.income_type,
                                                     transaction_time=payload.transaction_time.strftime(
                                                         '%Y-%m-%d %H:%M:%S'),
                                                     is_regular=payload.is_regular,
                                                     notes=payload.notes,
                                                     user_id=user.id
                                                     )
    record = Income_Manager.create(db=db, obj_in=data_in)

    return record
