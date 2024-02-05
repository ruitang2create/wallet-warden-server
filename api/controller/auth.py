from typing import Any

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm.session import Session

from api.depends import get_db
from db.schemas.user import CreateUserSchema
from db.models.user import User
from db.crud.crud_user import User_Manager

router = APIRouter()


@router.post("/signup", response_model=CreateUserSchema, status_code=201)
def create_user_signup(
        *,
        db: Session = Depends(get_db),
        payload: CreateUserSchema,
) -> Any:
    # user = db.query(User).filter(User.username = payload.username).first()
    user = User_Manager.get_by_username(db=db, username=payload.username)
    if user:
        raise HTTPException(
            status_code=400,
            detail="Username already exists"
        )
    user = User_Manager.create(db=db, obj_in=payload)

    return user
