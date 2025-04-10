from collections.abc import Callable

from presentation.ui.inventory_stocks import render_inventory_stocks
from presentation.ui.late_delivery_vouchers import render_late_delivery_vouchers
from presentation.ui.production_productivity import (
    render_production_productivity,
)
from presentation.ui.sales_statistics import render_sales_statistics
from presentation.ui.stop_sales_by_sectors import render_stop_sales_by_sectors

type Renderer = Callable[..., list[str]]


REPORT_TYPE_ID_TO_RENDERER: dict[str, Renderer] = {
    "late_delivery_vouchers": render_late_delivery_vouchers,
    "inventory_stocks": render_inventory_stocks,
    "sales": render_sales_statistics,
    "production_productivity": render_production_productivity,
    "stop_sales_by_sectors": render_stop_sales_by_sectors,
}
