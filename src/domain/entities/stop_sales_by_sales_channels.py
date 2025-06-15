from datetime import datetime

from pydantic import BaseModel

from src.domain.entities.enums.sales_channel import SalesChannel


class StopSaleBySalesChannel(BaseModel):
    unit_name: str
    started_at: datetime
    reason: str
    sales_channel: SalesChannel
