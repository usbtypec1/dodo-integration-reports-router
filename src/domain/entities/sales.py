from pydantic import BaseModel


class UnitSalesStatistics(BaseModel):
    unit_name: str
    sales_for_today: float
    growth_percentage: int


class TotalSalesStatistics(BaseModel):
    sales_for_today: float
    growth_percentage: int


class SalesStatisttics(BaseModel):
    units_breakdown: list[UnitSalesStatistics]
    total: TotalSalesStatistics
