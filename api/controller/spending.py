from sqlalchemy.orm import Session
from fastapi import Depends
from starlette.status import HTTP_201_CREATED

from api.depends import get_db
from api.server import app
from db.schemas.spending import GetSpendingListSchema, GetSpendingSchema, CreateSpendingSchema
from db.crud.crud_spending import Spending_Manager


@app.get("/spendings", response_model=GetSpendingListSchema)
def fetch_all_spendings(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    records = Spending_Manager.get_multi(db=db, skip=skip, limit=limit)
    return {
        "spendings": records,
    }


@app.get("/spendings/user/{user_id}", response_model=GetSpendingListSchema)
def fetch_all_spendings_by_user(user_id: str, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    print(f'Select spending records whose user_id = {user_id}')
    records = Spending_Manager.get_multi_by_user_id(db=db, user_id=user_id, skip=skip, limit=limit)
    return {
        "spendings": records,
    }


@app.post("/spending/user", response_model=GetSpendingSchema, status_code=HTTP_201_CREATED)
def create_spending(payload: CreateSpendingSchema, db: Session = Depends(get_db)):
    record = Spending_Manager.create(db=db, obj_in=payload)

    return record


