from typing import Optional, Any
from sqlalchemy.orm import Session

from auth.auth_security import hash_password
from db.crud.base import CRUDBase
from db.models.user import User
from db.schemas.user import CreateUserSchema


class CRUDUser(CRUDBase[User, CreateUserSchema]):
    def create(self, db: Session, *, obj_in: CreateUserSchema) -> User:
        create_data = obj_in.dict()
        create_data.pop("password")
        db_obj = User(**create_data)
        db_obj.hashed_password = hash_password(obj_in.password)
        db.add(db_obj)
        db.commit()

        return db_obj

    def get_by_username(self, db: Session, username: str) -> Optional[User]:
        return db.query(User).filter(self.model.username == username).first()


User_Manager = CRUDUser(User)
