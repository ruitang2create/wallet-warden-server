from pydantic import BaseModel, UUID4


class UserBase(BaseModel):
    username: str


class CreateUserSchema(UserBase):
    password: str


class UserInDBBase(UserBase):
    id: UUID4

    class Config:
        orm_mode = True


# Additional properties stored in DB but not returned by API
class UserInDB(UserInDBBase):
    hashed_password: str


# Additional properties to return via API
class UserResponseSchema(UserInDBBase):
    ...
