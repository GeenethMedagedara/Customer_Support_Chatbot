from pydantic import BaseModel
from typing import List

class ProductRequest(BaseModel):
    category: str

class Product(BaseModel):
    product_id: int
    category: str
    description: str
    name: str
    price: float
    quantity: int
    rating: float
    status: str
