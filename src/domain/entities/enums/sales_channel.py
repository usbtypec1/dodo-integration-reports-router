from enum import StrEnum, auto


class SalesChannel(StrEnum):
    DINE_IN = auto()
    TAKEAWAY = auto()
    DELIVERY = auto()


class StopSaleSalesChannel(StrEnum):
    DINE_IN = "Dine-in"
    TAKEAWAY = "Takeaway"
    DELIVERY = "Delivery"
