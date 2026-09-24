from uuid import UUID

from pydantic import BaseModel, EmailStr
# from sqlalchemy import UUID

class UserCreate(BaseModel):
    name: str
    email: EmailStr

class ProductCreate(BaseModel):
    name: str
    description: str
    price: float
    inventory_count: int

class OrderItemRequest(BaseModel):
    product_id: UUID
    quantity: int

class OrderCreate(BaseModel):
    user_id: UUID
    items: list[OrderItemRequest]