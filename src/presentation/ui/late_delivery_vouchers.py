from collections.abc import Iterable
from typing import TypedDict

from aiogram.utils.formatting import Bold

from presentation.i18n import gettext as _


class UnitLateDeliveryVoucherStatistics(TypedDict):
    unit_name: str
    vouchers_for_today_count: int
    vouchers_for_week_before_count: int


def render_late_delivery_vouchers(
    units_statistics: Iterable[UnitLateDeliveryVoucherStatistics],
) -> str:
    lines: list[str] = [Bold(_("render:late_delivery_vouchers:title")).as_html()]
    unit_message = _("render:late_delivery_vouchers:unit")

    for unit in units_statistics:
        lines.append(
            f"{unit['unit_name']}"
            f" | {unit['vouchers_for_today_count']} {unit_message}"
            f" | {unit['vouchers_for_week_before_count']} {unit_message}"
        )

    return "\n".join(lines)
