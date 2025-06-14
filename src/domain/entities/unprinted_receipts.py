from pydantic import BaseModel


class OrderWithoutPrintedReceipt(BaseModel):
    number: str
    price: int


class UnitUnprintedReceipts(BaseModel):
    unit_name: str
    orders: list[OrderWithoutPrintedReceipt]
