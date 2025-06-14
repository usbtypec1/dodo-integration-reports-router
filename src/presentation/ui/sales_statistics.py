from aiogram.utils.formatting import Bold

from domain.entities.sales import SalesStatisttics
from presentation.i18n import gettext as _
from presentation.ui.common import format_percentage, int_gaps


def render_sales_statistics(
    sales_statistics: SalesStatisttics,
) -> list[str]:
    lines: list[str] = [Bold(_("render:sales_statistics:title")).as_html()]

    units_sales_statistics = sorted(
        sales_statistics.units_breakdown,
        key=lambda unit: unit.sales_for_today,
        reverse=True,
    )

    for unit_sales_statistics in units_sales_statistics:
        lines.append(
            f"{unit_sales_statistics.unit_name}"
            f" | {int_gaps(unit_sales_statistics.sales_for_today)}"
            f" | {format_percentage(unit_sales_statistics.growth_percentage)}"
        )

    total_sales = int_gaps(sales_statistics.total.sales_for_today)
    total_growth_percentage = format_percentage(
        sales_statistics.total.growth_percentage,
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
