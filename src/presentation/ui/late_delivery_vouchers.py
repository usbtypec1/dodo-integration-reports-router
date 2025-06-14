from collections.abc import Iterable
from typing import override

from aiogram.utils.formatting import Bold

from domain.entities.late_delivery_vouchers import (
    UnitLateDeliveryVoucherStatistics,
)
from presentation.i18n import gettext as _
from presentation.ui.base import TextView


class LateDeliveryVouchersView(TextView):
    def __init__(self, payload: Iterable[UnitLateDeliveryVoucherStatistics]) -> None:
        self.__units_statistics = payload

    @override
    def get_texts(self) -> list[str]:
        lines: list[str] = [Bold(_("render:late_delivery_vouchers:title")).as_html()]
        unit_message = _("render:late_delivery_vouchers:unit")

        for unit in self.__units_statistics:
            lines.append(
                f"{unit.unit_name}"
                f" | {unit.vouchers_count_for_today} {unit_message}"
                f" | {unit.vouchers_count_for_week_before} {unit_message}"
            )

        return ["\n".join(lines)]
