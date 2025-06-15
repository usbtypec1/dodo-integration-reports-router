from pydantic import BaseModel


class UnitHeatedShelfStatistics(BaseModel):
    unit_name: str
    average_heated_shelf_time_in_seconds: int
    trips_with_one_orders_percentage: int
