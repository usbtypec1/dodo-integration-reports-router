from typing import override

from aiogram.utils.formatting import Bold

from domain.entities.sales import SalesStatisttics
from presentation.i18n import gettext as _
from presentation.ui.base import TextView
from presentation.ui.common import format_percentage, int_gaps


class SalesStatisticsView(TextView):
    def __init__(self, payload: SalesStatisttics):
        self.__sales_statistics = payload

    @override
    def get_texts(self) -> list[str]:
        lines: list[str] = [Bold(_("render:sales_statistics:title")).as_html()]

        units_sales_statistics = sorted(
            self.__sales_statistics.units_breakdown,
            key=lambda unit: unit.sales_for_today,
            reverse=True,
        )

        for unit_sales_statistics in units_sales_statistics:
            lines.append(
                f"{unit_sales_statistics.unit_name}"
                f" | {int_gaps(unit_sales_statistics.sales_for_today)}"
                f" | {format_percentage(unit_sales_statistics.growth_percentage)}"
            )

        total_sales = int_gaps(self.__sales_statistics.total.sales_for_today)
        total_growth_percentage = format_percentage(
            self.__sales_statistics.total.growth_percentage,
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
