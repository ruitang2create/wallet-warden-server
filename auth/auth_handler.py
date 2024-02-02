import time
from typing import Dict

import jwt
from decouple import config

jwt_secret = config("JWT_SECRET")
jwt_algo = config("JWT_ALGORITHM")
jwt_life = config("JWT_LIFE")


def token_response(token: str):
    return {
        "access_token": token
    }


def sign_jwt(user_id: str) -> Dict[str, str]:
    payload = {
        "user_id": user_id,
        "expires": time.time() + jwt_life
    }
    token = jwt.encode(payload, jwt_secret, algorithm=jwt_algo)

    return token_response(token)


def decode_jwt(token: str) -> dict:
    try:
        decoded_token = jwt.decode(token, jwt_secret, algorithms=[jwt_algo])
        return decoded_token if decoded_token["expires"] >= time.time() else None
    except:
        return {}
