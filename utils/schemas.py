from pydantic import BaseModel


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    user_id: int | None = None


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


class UserOut(BaseModel):
    id: int
    email: str

    first_name: str
    last_name: str


class UserLoginIn(BaseModel):
    email: str
    password: str


class UserList(BaseModel):
    user_list: list[User]
