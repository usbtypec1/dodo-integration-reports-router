from domain.entities.unprinted_receipts import UnitUnprintedReceipts
from presentation.i18n import gettext as _
from presentation.ui.base import TextView
from presentation.ui.common import int_gaps


class UnitUnprintedReceiptsView(TextView):
    def __init__(self, payload: UnitUnprintedReceipts):
        self.__unit_unprinted_receipts = payload

    def get_text(self) -> str:
        unit_name = self.__unit_unprinted_receipts.unit_name
        orders = self.__unit_unprinted_receipts.orders

        lines: list[str] = [
            "Менеджер, привет!",
            f"<b>В пиццерии {unit_name} есть незакрытые чеки,</b>"
            " пожалуйста, проверь информацию и закрой все чеки:",
        ]

        for order in orders:
            lines.append(f"{order.number} / {int_gaps(order.price)}")

        return "\n".join(lines)
