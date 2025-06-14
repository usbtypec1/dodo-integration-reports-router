from pydantic import BaseModel


class UnitProductionProductivityStatistics(BaseModel):
    unit_name: str
    sales_per_labor_hour_for_today: float
    growth_percentage: int
