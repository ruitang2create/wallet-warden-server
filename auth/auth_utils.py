from typing import Dict, Optional
import time
from datetime import datetime
import jwt
from decouple import config
from sqlalchemy.orm.session import Session

from db.models.user import User
from db.crud.crud_user import User_Manager
from auth.auth_security import verify_password

jwt_secret = config("JWT_SECRET")
jwt_algo = config("JWT_ALGORITHM")
jwt_life = config("JWT_LIFE")


def authenticate(
        *,
        username: str,
        password: str,
        db: Session
) -> Optional[User]:
    user = User_Manager.get_by_username(db=db, username=username)
    if not user:
        return None
    if not verify_password(password, user.hashed_password):
        return None

    return user


def token_response(token: str):
    return {
        "access_token": token,
        "token_type": "bearer",
    }


def sign_jwt(user_id: str) -> Dict[str, str]:
    payload = {
        "sub": user_id,
        "exp": time.time() + int(jwt_life),
        "iat": time.time()
    }
    token = jwt.encode(payload, jwt_secret, algorithm=jwt_algo)

    return token_response(token)


def decode_jwt(token: str) -> dict:
    decoded_token = jwt.decode(token, jwt_secret, algorithms=jwt_algo)
    return decoded_token if decoded_token["exp"] >= time.time() else None
