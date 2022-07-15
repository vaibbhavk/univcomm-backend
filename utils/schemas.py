from pydantic import BaseModel
import datetime


class ItemBase(BaseModel):
    title: str
    description: str | None = None


class ItemCreate(ItemBase):
    pass


class Item(ItemBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: bool
    items: list[Item] = []

    class Config:
        orm_mode = True

class AdminIn(BaseModel):
    email: str
    password: str

class AdminOut(BaseModel):
    id: int
    email: str

class UserIn(BaseModel):
    email: str
    password: str

    first_name: str
    last_name: str
    guardian: str
    dob: datetime.date
    address: str
    contact: str

class UserOut(BaseModel):
    id: int
    email: str

class UserLoginIn(BaseModel):
    email: str
    password: str

class UserList(BaseModel):
    user_list: list[User]