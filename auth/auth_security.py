from passlib.context import CryptContext

PWD_CONTEXT = CryptContext(schemes=["bcrypt"])


def verify_password(unverified_password: str, hashed_password: str) -> bool:
    return PWD_CONTEXT.verify(unverified_password, hashed_password)


def hash_password(raw_password: str) -> str:
    return PWD_CONTEXT.hash(raw_password)
