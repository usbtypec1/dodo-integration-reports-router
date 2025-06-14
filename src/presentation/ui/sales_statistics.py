from typing import TypedDict

from aiogram.utils.formatting import Bold

from presentation.i18n import gettext as _
from presentation.ui.common import format_percentage, int_gaps


class UnitSalesStatistics(TypedDict):
    unit_name: str
    sales_for_today: float
    growth_percentage: int


class TotalSalesStatistics(TypedDict):
    sales_for_today: float
    growth_percentage: int


class SalesStatisttics(TypedDict):
    units_breakdown: list[UnitSalesStatistics]
    total: TotalSalesStatistics


def render_sales_statistics(
    sales_statistics: SalesStatisttics,
) -> list[str]:
    lines: list[str] = [Bold(_("render:sales_statistics:title")).as_html()]

    units_sales_statistics = sorted(
        sales_statistics["units_breakdown"],
        key=lambda unit: unit["sales_for_today"],
        reverse=True,
    )

    for unit_sales_statistics in units_sales_statistics:
        unit_name = unit_sales_statistics["unit_name"]
        sales_for_today = unit_sales_statistics["sales_for_today"]
        growth_percentage = unit_sales_statistics["growth_percentage"]

        lines.append(
            f"{unit_name}"
            f" | {int_gaps(sales_for_today)}"
            f" | {format_percentage(growth_percentage)}"
        )

    total_sales = int_gaps(sales_statistics["total"]["sales_for_today"])
    total_growth_percentage = format_percentage(
        sales_statistics["total"]["growth_percentage"]
    )

    lines.append(
        Bold(
            _("render:sales_statistics:total")
            % {
                "sales": total_sales,
                "growth_percentage": total_growth_percentage,
            },
        ).as_html()
    )
    return ["\n".join(lines)]
