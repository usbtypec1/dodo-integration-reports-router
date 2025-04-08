from collections.abc import Iterable
from typing import TypedDict

from aiogram.utils.formatting import Bold

from presentation.i18n import gettext as _


class UnitLateDeliveryVoucherStatistics(TypedDict):
    unit_name: str
    vouchers_count_for_today: int
    vouchers_count_for_week_before: int


def render_late_delivery_vouchers(
    units_statistics: Iterable[UnitLateDeliveryVoucherStatistics],
) -> list[str]:
    lines: list[str] = [Bold(_("render:late_delivery_vouchers:title")).as_html()]
    unit_message = _("render:late_delivery_vouchers:unit")

    for unit in units_statistics:
        lines.append(
            f"{unit['unit_name']}"
            f" | {unit['vouchers_count_for_today']} {unit_message}"
            f" | {unit['vouchers_count_for_week_before']} {unit_message}"
        )

    return ["\n".join(lines)]
