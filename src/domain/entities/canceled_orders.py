from uuid import UUID

from pydantic import BaseModel

from domain.entities.enums.country_code import CountryCode
from domain.entities.enums.sales_channel import SalesChannel


class CanceledOrder(BaseModel):
    id: UUID
    number: str
    price: int
    sales_channel: SalesChannel
    is_refund_receipt_printed: bool


class UnitCanceledOrders(BaseModel):
    unit_name: str
    orders: list[CanceledOrder]
    country_code: CountryCode
