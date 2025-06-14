from pydantic import BaseModel

from domain.entities.enums.measurement_unit import MeasurementUnit


class UnitInventoryStockItem(BaseModel):
    name: str
    quantity: float
    measurement_unit: MeasurementUnit


class UnitInventoryStocks(BaseModel):
    unit_name: str
    items: list[UnitInventoryStockItem]
