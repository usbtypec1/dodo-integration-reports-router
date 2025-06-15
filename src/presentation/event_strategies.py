from typing import Any, Protocol

from pydantic import BaseModel, TypeAdapter

from domain.entities.inventory_stocks import UnitInventoryStocks
from domain.entities.late_delivery_vouchers import (
    UnitLateDeliveryVoucherStatistics,
)
from domain.entities.production_productivity import (
    UnitProductionProductivityStatistics,
)
from domain.entities.sales import SalesStatisttics
from domain.entities.stop_sales_by_sectors import UnitStopSalesBySectors
from presentation.ui.base import ReplyMarkup
from presentation.ui.inventory_stocks import InventoryStocksView
from presentation.ui.late_delivery_vouchers import LateDeliveryVouchersView
from presentation.ui.production_productivity import (
    ProductionProductivityView,
)
from presentation.ui.sales_statistics import SalesStatisticsView
from presentation.ui.stop_sales_by_sectors import StopSalesBySectorsView

type PydanticModel = type[BaseModel] | TypeAdapter


def parse_payload(
    payload: dict | list,
    pydantic_model: PydanticModel,
) -> BaseModel:
    if isinstance(pydantic_model, TypeAdapter):
        return pydantic_model.validate_python(payload)
    return pydantic_model.model_validate(payload)


class ReportView(Protocol):
    def __init__(self, payload: Any) -> None: ...

    def get_texts(self) -> list[str]: ...

    def get_reply_markup(self) -> ReplyMarkup | None: ...


REPORT_TYPE_ID_TO_RENDERER_AND_PYDANTIC_MODEL: dict[
    str, tuple[type[ReportView], PydanticModel]
] = {
    "late_delivery_vouchers": (
        LateDeliveryVouchersView,
        TypeAdapter(list[UnitLateDeliveryVoucherStatistics]),
    ),
    "inventory_stocks": (
        InventoryStocksView,
        TypeAdapter(list[UnitInventoryStocks]),
    ),
    "sales": (
        SalesStatisticsView,
        SalesStatisttics,
    ),
    "production_productivity": (
        ProductionProductivityView,
        TypeAdapter(list[UnitProductionProductivityStatistics]),
    ),
    "stop_sales_by_sectors": (
        StopSalesBySectorsView,
        TypeAdapter(list[UnitStopSalesBySectors]),
    ),
}
