from sqlalchemy.orm import Session
from fastapi import Depends, APIRouter, HTTPException, status
from starlette.status import HTTP_201_CREATED

from api.depends import get_db, get_current_user
from db.schemas.spending import SpendingListResponseSchema, SpendingResponseSchema, CreateSpendingSchema, \
    CreateSpendingRequestSchema
from db.crud.crud_spending import Spending_Manager

router = APIRouter()


@router.get("/", response_model=SpendingListResponseSchema)
def fetch_all_spendings(skip: int = 0, limit: int = 100, db: Session = Depends(get_db), user=Depends(get_current_user)):
    if not user.is_superuser:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Unauthorized request"
        )
    records = Spending_Manager.get_multi(db=db, skip=skip, limit=limit)
    return {
        "spendings": records,
    }


@router.get("/user", response_model=SpendingListResponseSchema)
def fetch_all_spendings_by_user(skip: int = 0, limit: int = 100, db: Session = Depends(get_db),
                                user=Depends(get_current_user)):
    print(f'Select spending records whose user_id = {user.id}')
    records = Spending_Manager.get_multi_by_user_id(db=db, user_id=user.id, skip=skip, limit=limit)
    return {
        "spendings": records,
    }


@router.post("/user", response_model=SpendingResponseSchema, status_code=HTTP_201_CREATED)
def create_spending(payload: CreateSpendingRequestSchema, db: Session = Depends(get_db),
                    user=Depends(get_current_user)):
    data_in: CreateSpendingSchema = CreateSpendingSchema(recipient=payload.recipient,
                                                         amount=payload.amount,
                                                         currency=payload.currency,
                                                         spending_type=payload.spending_type,
                                                         transaction_time=payload.transaction_time.strftime(
                                                             '%Y-%m-%d %H:%M:%S'),
                                                         is_necessary=payload.is_necessary,
                                                         notes=payload.notes,
                                                         user_id=user.id
                                                         )
    record = Spending_Manager.create(db=db, obj_in=data_in)

    return record
