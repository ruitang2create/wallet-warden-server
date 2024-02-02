from pydantic import BaseModel, UUID4


class CreateUserSchema(BaseModel):
    username: str
    password: str

