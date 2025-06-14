from pydantic import BaseModel


class UnitLateDeliveryVoucherStatistics(BaseModel):
    unit_name: str
    vouchers_count_for_today: int
    vouchers_count_for_week_before: int
