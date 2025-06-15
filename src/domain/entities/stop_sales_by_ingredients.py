import datetime

from pydantic import BaseModel


class StopSaleByIngredient(BaseModel):
    started_at: datetime.datetime
    ingredient_name: str


class StopSalesByIngredientsGroupedByReason(BaseModel):
    reason: str
    stop_sales: list[StopSaleByIngredient]


class UnitStopSalesByIngredients(BaseModel):
    unit_name: str
    stop_sales_grouped_by_reasons: list[StopSalesByIngredientsGroupedByReason]
