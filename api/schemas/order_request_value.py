from pydantic import BaseModel

class OrderRequest(BaseModel):
    order_id: int

class Order(BaseModel):
    order_id: int
    name: str
    qty: int
    status: str
    total: float
