from pydantic import BaseModel


class StopSale(BaseModel):
    sector_name: str
    started_at: str


class UnitStopSalesBySectors(BaseModel):
    unit_name: str
    stop_sales: list[StopSale]
    timezone: str
