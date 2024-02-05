from typing import Any

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm.session import Session

from api.depends import get_db
from db.schemas.user import CreateUserSchema, UserResponseSchema
from db.crud.crud_user import User_Manager
from auth.auth_utils import authenticate, sign_jwt

router = APIRouter()


@router.post("/signup", response_model=UserResponseSchema, status_code=201)
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


@router.post("/login")
def login(
        payload: CreateUserSchema,
        db: Session = Depends(get_db),
) -> Any:
    user = authenticate(username=payload.username, password=payload.password, db=db)
    if not user:
        raise HTTPException(
            status_code=400,
            detail="Incorrect username or password"
        )
    jwt_response = sign_jwt(user.id)

    return jwt_response
