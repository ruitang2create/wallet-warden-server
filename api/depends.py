from typing import Generator
from fastapi import Depends, HTTPException, status, Security
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from sqlalchemy.orm.session import Session
from jwt import PyJWTError

from db.crud.crud_user import User_Manager
from db.session import LocalSession
from db.models.user import User
from auth.auth_utils import decode_jwt

security = HTTPBearer()


def get_db() -> Generator:
    db = LocalSession()
    try:
        yield db
    finally:
        db.close()


def get_current_user(
        db: Session = Depends(get_db),
        token: HTTPAuthorizationCredentials = Security(security)
) -> User:
    try:
        payload = decode_jwt(token.credentials)
        if payload is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Token expired",
                headers={"WWW-Authenticate": "Bearer"},
            )
    except PyJWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token",
            headers={"WWW-Authenticate": "Bearer"},
        )
    user = User_Manager.get(db=db, id=payload["sub"])
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not verify credentials",
        )
    return user

