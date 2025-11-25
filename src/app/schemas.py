from pydantic import BaseModel
from typing import Optional

class User_create(BaseModel):
    name: str
    email: str
    password: str

    class Config:
        from_attributes = True

class Login(BaseModel):
    email: str
    password: str

    class Config:
        from_attributes = True

class User_read(BaseModel):
    id: int
    name: str
    email: str
    active: bool
    admin: bool

    class Config:
        from_attributes = True

class Order_create(BaseModel):
    user: int

    class Config:
        from_attributes = True

class Item_schema(BaseModel):
    name: str
    amount: int
    flavor: str
    unit_price: float
    size: str

    class Config:
        from_attributes = True

class Order_read(BaseModel):
    id: int
    status: str
    user: User_read
    price: float 
    itens: list[Item_schema]

    class Config:
        from_attributes = True