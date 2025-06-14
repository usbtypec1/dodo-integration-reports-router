import datetime

from pydantic import BaseModel


class FraudOrder(BaseModel):
    created_at: datetime.datetime
    number: str


class UnitFraudOrders(BaseModel):
    unit_name: str
    phone_number: str
    orders: list[FraudOrder]
