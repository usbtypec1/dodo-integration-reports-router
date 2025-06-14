from pydantic import BaseModel


class UnitDeliverySpeedStatistics(BaseModel):
    unit_name: str
    average_cooking_time_in_seconds: int
    average_delivery_order_fulfillment_time_in_seconds: int
    average_heated_shelf_time_in_seconds: int
    average_order_trip_time_in_seconds: int
