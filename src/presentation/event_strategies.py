from collections.abc import Callable

from presentation.ui.inventory_stocks import render_inventory_stocks
from presentation.ui.late_delivery_vouchers import render_late_delivery_vouchers

type Renderer = Callable[..., list[str]]


REPORT_TYPE_ID_TO_RENDERER: dict[str, Renderer] = {
    "late_delivery_vouchers": render_late_delivery_vouchers,
    "inventory_stocks": render_inventory_stocks,
}
