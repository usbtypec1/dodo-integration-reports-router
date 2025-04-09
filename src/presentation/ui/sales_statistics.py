from collections.abc import Iterable
from typing import TypedDict

from aiogram.utils.formatting import Bold

from presentation.i18n import gettext as _


class UnitSalesStatistics(TypedDict):
    unit_name: str
    sales_for_today: float
    growth_percentage: int


def int_gaps(number: int | float) -> str:
    return f"{number:_}".replace("_", " ")


def display_percentage(number: int | float) -> str:
    return f"{number:+}%"


def render_sales_statistics(
    units_sales_statistics: Iterable[UnitSalesStatistics],
) -> list[str]:
    lines: list[str] = [Bold(_("render:sales_statistics:title")).as_html()]
    for unit_sales_statistics in units_sales_statistics:
        unit_name = unit_sales_statistics["unit_name"]
        sales_for_today = unit_sales_statistics["sales_for_today"]
        growth_percentage = unit_sales_statistics["growth_percentage"]

        lines.append(
            f"{unit_name}"
            f" | {int_gaps(sales_for_today)}"
            f" | {display_percentage(growth_percentage)}"
        )
    return ["\n".join(lines)]
