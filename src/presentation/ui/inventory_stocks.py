from collections.abc import Iterable
from typing import override

from aiogram.utils.formatting import Bold

from domain.entities.enums.measurement_unit import MeasurementUnit
from domain.entities.inventory_stocks import UnitInventoryStocks
from presentation.i18n import gettext as _
from presentation.ui.base import TextView

measurement_unit_map = {
    MeasurementUnit.QUANTITY: _("render:inventory_stocks:measurement_unit:quantity"),
    MeasurementUnit.KILOGRAM: _("render:inventory_stocks:measurement_unit:kilogram"),
    MeasurementUnit.LITER: _("render:inventory_stocks:measurement_unit:liter"),
    MeasurementUnit.METER: _("render:inventory_stocks:measurement_unit:meter"),
}


class InventoryStocksView(TextView):
    def __init__(self, payload: Iterable[UnitInventoryStocks]) -> None:
        self.__units_inventory_stocks = payload

    @override
    def get_texts(self) -> list[str]:
        texts: list[str] = []
        for unit_inventory_stocks in self.__units_inventory_stocks:
            lines: list[str] = [
                unit_inventory_stocks.unit_name,
                Bold(_("render:inventory_stocks:runs_out_today")).as_html(),
            ]

            for item in unit_inventory_stocks.items:
                stock_word = _("render:inventory_stocks:remaining")
                measurement_unit = measurement_unit_map.get(
                    item.measurement_unit,
                    item.measurement_unit,
                )
                lines.append(
                    f"📍 {item.name} - {stock_word}:"
                    f" <b><u>{item.quantity} {measurement_unit}</u></b>"
                )
            texts.append("\n".join(lines))

        return texts
