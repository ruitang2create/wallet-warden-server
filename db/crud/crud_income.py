from sqlalchemy.orm import Session

from db.crud.base import CRUDBase
from db.models.income import Income
from db.schemas.income import CreateIncomeSchema


class CRUDIncome(CRUDBase[Income, CreateIncomeSchema]):
    def get_multi_by_user_id(self, *, db: Session, user_id: str, skip: int = 0, limit: int = 100):
        return db.query(self.model).filter_by(user_id=user_id).offset(skip).limit(limit).all()


Income_Manager = CRUDIncome(Income)
