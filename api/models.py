

from pydantic import BaseModel


class User(BaseModel):
    email: str
    password: str


class UserUI(BaseModel):
    id: int
    email: str
