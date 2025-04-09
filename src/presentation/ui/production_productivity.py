from collections.abc import Iterable
from typing import TypedDict

from aiogram.utils.formatting import Bold

from presentation.i18n import gettext as _
from presentation.ui.common import format_percentage, int_gaps


class UnitProductionProductivityStatistics(TypedDict):
    unit_name: str
    sales_per_labor_hour_for_today: float
    growth_percentage: int


def render_production_productivity(
    units_production_productivity_statistics: Iterable[
        UnitProductionProductivityStatistics
    ],
) -> list[str]:
    lines: list[str] = [Bold(_("render:production_productivity:title")).as_html()]

    units_production_productivity_statistics = sorted(
        units_production_productivity_statistics,
        key=lambda unit: unit["sales_per_labor_hour_for_today"],
        reverse=True,
    )
    for unit_statistics in units_production_productivity_statistics:
        unit_name: str = unit_statistics["unit_name"]
        sales_per_labor_hour_for_today: float = unit_statistics[
            "sales_per_labor_hour_for_today"
        ]
        growth_percentage: int = unit_statistics["growth_percentage"]

        lines.append(
            f"{unit_name}"
            f" | {int_gaps(sales_per_labor_hour_for_today)}"
            f" | {format_percentage(growth_percentage)}"
        )

    return "\n".join(lines)
