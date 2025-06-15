import operator
from collections.abc import Iterable
from typing import Final, override
from uuid import UUID

from domain.entities.canceled_orders import CanceledOrder, UnitCanceledOrders
from domain.entities.enums.country_code import CountryCode
from domain.entities.enums.sales_channel import SalesChannel
from presentation.i18n import gettext as _
from presentation.ui.base import TextView

SALES_CHANNEL_TO_NAME: Final[dict[SalesChannel, str]] = {
    SalesChannel.DINE_IN: "Ресторан",
    SalesChannel.TAKEAWAY: "Самовывоз",
    SalesChannel.DELIVERY: "Доставка",
}

COUNTRY_CODE_TO_CURRENCY_SYMBOL: Final[dict[CountryCode, str]] = {
    CountryCode.RU: "₽",
    CountryCode.EE: "€",
}


def build_order_url(
    *,
    country_code: CountryCode,
    order_id: UUID,
) -> str:
    return (
        f"https://shiftmanager.dodopizza.{country_code}"
        f"/Managment/ShiftManagment/Order?orderUUId={order_id.hex}"
    )


def compute_total_price(orders: Iterable[CanceledOrder]) -> int:
    return sum(order.price for order in orders)


def sort_orders_by_printed_receipt(
    orders: Iterable[CanceledOrder],
) -> list[CanceledOrder]:
    return sorted(
        orders,
        key=operator.attrgetter("is_refund_receipt_printed"),
        reverse=True,
    )


def render_canceled_order(
    *,
    order: CanceledOrder,
    country_code: CountryCode,
    currency_symbol: str,
) -> str:
    lines: list[str] = []

    order_url = build_order_url(
        country_code=country_code,
        order_id=order.id,
    )

    if not order.is_refund_receipt_printed:
        no_receipt_message = _("render:canceled_orders:no_receipt")
        lines.append(no_receipt_message)

    order_message = _("render:canceled_orders:order") % {
        "url": order_url,
        "number": order.number,
        "price": order.price,
        "currency_symbol": currency_symbol,
    }
    order_type_message = _("render:canceled_orders:order_type") % {
        "type": order.sales_channel.value
    }

    lines.append(order_message)
    lines.append(order_type_message)

    return "\n".join(lines)


def render_canceled_orders(
    *,
    orders: Iterable[CanceledOrder],
    country_code: CountryCode,
    currency_symbol: str,
) -> str:
    lines = [
        render_canceled_order(
            order=order,
            country_code=country_code,
            currency_symbol=currency_symbol,
        )
        for order in orders
    ]
    return "\n\n".join(lines)


class UnitCanceledOrdersView(TextView):
    def __init__(self, payload: UnitCanceledOrders):
        self.__unit_canceled_orders = payload

    @override
    def get_texts(self) -> list[str]:
        country_code = self.__unit_canceled_orders.country_code
        currency_symbol = COUNTRY_CODE_TO_CURRENCY_SYMBOL.get(country_code, "")

        orders = sort_orders_by_printed_receipt(
            orders=self.__unit_canceled_orders.orders,
        )
        orders_text = render_canceled_orders(
            orders=orders,
            country_code=country_code,
            currency_symbol=currency_symbol,
        )
        total_price = compute_total_price(self.__unit_canceled_orders.orders)

        title = _("render:canceled_orders:unit_report_title") % {
            "unit_name": self.__unit_canceled_orders.unit_name
        }
        total = _("render:canceled_orders:total") % {
            "total_price": total_price,
            "currency_symbol": currency_symbol,
        }

        return [f"{title}\n\n{orders_text}\n\n{total}"]
