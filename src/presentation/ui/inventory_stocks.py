from collections.abc import Iterable
from typing import Literal, TypedDict

from aiogram.utils.formatting import Bold

from presentation.i18n import gettext as _


class UnitInventoryStockItem(TypedDict):
    name: str
    quantity: float
    measurement_unit: Literal["Quantity", "Kilogram", "Liter", "Meter"]


class UnitInventoryStocks(TypedDict):
    unit_name: str
    items: list[UnitInventoryStockItem]


def render_inventory_stocks(
    units_inventory_stocks: Iterable[UnitInventoryStocks],
) -> list[str]:
    measurement_unit_map = {
        "Quantity": _("render:inventory_stocks:measurement_unit:quantity"),
        "Kilogram": _("render:inventory_stocks:measurement_unit:kilogram"),
        "Liter": _("render:inventory_stocks:measurement_unit:liter"),
        "Meter": _("render:inventory_stocks:measurement_unit:meter"),
    }

    texts: list[str] = []
    for unit_inventory_stocks in units_inventory_stocks:
        lines: list[str] = [
            unit_inventory_stocks["unit_name"],
            Bold(_("render:inventory_stocks:runs_out_today")).as_html(),
        ]
        for item in unit_inventory_stocks["items"]:
            stock_word = _("render:inventory_stocks:remaining")
            measurement_unit = measurement_unit_map.get(
                item["measurement_unit"],
                item["measurement_unit"],
            )
            lines.append(
                f"📍 {item['name']} - {stock_word}:"
                f" <b><u>{item['quantity']} {measurement_unit}</u></b>"
            )
        texts.append("\n".join(lines))
    return texts
