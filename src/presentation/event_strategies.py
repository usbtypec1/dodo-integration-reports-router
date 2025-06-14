from collections.abc import Callable

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
from presentation.ui.inventory_stocks import render_inventory_stocks
from presentation.ui.late_delivery_vouchers import render_late_delivery_vouchers
from presentation.ui.production_productivity import (
    render_production_productivity,
)
from presentation.ui.sales_statistics import render_sales_statistics
from presentation.ui.stop_sales_by_sectors import render_stop_sales_by_sectors

type Renderer = Callable[..., list[str]]
type PydanticModel = type[BaseModel] | TypeAdapter


def parse_payload(
    payload: dict | list,
    pydantic_model: PydanticModel,
) -> BaseModel:
    if isinstance(pydantic_model, TypeAdapter):
        return pydantic_model.validate_python(payload)
    return pydantic_model.model_validate(payload)


REPORT_TYPE_ID_TO_RENDERER_AND_PYDANTIC_MODEL: dict[
    str, tuple[Renderer, PydanticModel]
] = {
    "late_delivery_vouchers": (
        render_late_delivery_vouchers,
        TypeAdapter(list[UnitLateDeliveryVoucherStatistics]),
    ),
    "inventory_stocks": (
        render_inventory_stocks,
        TypeAdapter(list[UnitInventoryStocks]),
    ),
    "sales": (
        render_sales_statistics,
        SalesStatisttics,
    ),
    "production_productivity": (
        render_production_productivity,
        TypeAdapter(list[UnitProductionProductivityStatistics]),
    ),
    "stop_sales_by_sectors": (
        render_stop_sales_by_sectors,
        TypeAdapter(list[UnitStopSalesBySectors]),
    ),
}
