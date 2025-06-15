from collections.abc import Iterable
from typing import override

from aiogram.utils.formatting import Bold

from domain.entities.production_productivity import (
    UnitProductionProductivityStatistics,
)
from presentation.i18n import gettext as _
from presentation.ui.base import TextView
from presentation.ui.common import format_percentage, int_gaps


class ProductionProductivityView(TextView):
    def __init__(
        self,
        payload: Iterable[UnitProductionProductivityStatistics],
    ) -> None:
        self.__units_production_productivity_statistics = payload

    @override
    def get_texts(self) -> list[str]:
        lines: list[str] = [Bold(_("render:production_productivity:title")).as_html()]

        units_production_productivity_statistics = sorted(
            self.__units_production_productivity_statistics,
            key=lambda unit: unit.sales_per_labor_hour_for_today,
            reverse=True,
        )
        for unit_statistics in units_production_productivity_statistics:
            lines.append(
                f"{unit_statistics.unit_name}"
                f" | {int_gaps(unit_statistics.sales_per_labor_hour_for_today)}"
                f" | {format_percentage(unit_statistics.growth_percentage)}"
            )

        return ["\n".join(lines)]
