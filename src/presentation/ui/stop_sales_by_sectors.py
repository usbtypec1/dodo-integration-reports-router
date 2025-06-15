import datetime
from collections.abc import Iterable
from typing import Final, override
from zoneinfo import ZoneInfo

import humanize

from domain.entities.stop_sales_by_sectors import UnitStopSalesBySectors
from presentation.i18n import gettext as _
from presentation.ui.base import TextView

MINUTE_IN_SECONDS: Final[int] = 60
HOUR_IN_SECONDS: Final[int] = MINUTE_IN_SECONDS * 60
DAY_IN_SECONDS: Final[int] = HOUR_IN_SECONDS * 24

type TimeUnitsAndAbbreviation = tuple[tuple[str, ...], str]


def parse_datetime(
    date_string: str,
    timezone: ZoneInfo,
) -> datetime.datetime:
    return datetime.datetime.fromisoformat(date_string).astimezone(timezone)


def abbreviate_time_units(text: str) -> str:
    time_units_and_abbreviations: tuple[TimeUnitsAndAbbreviation, ...] = (
        (("дней", "день", "дня"), "дн"),
        (
            (
                "часов",
                "часа",
                "час",
            ),
            "ч",
        ),
        (("минута", "минуты", "минут"), "мин"),
    )
    words = set(text.split())
    for time_units, abbreviation in time_units_and_abbreviations:
        for time_unit in time_units:
            if time_unit not in words:
                continue
            text = text.replace(time_unit, abbreviation)
    return text


def compute_duration(
    started_at: datetime.datetime,
    timezone: ZoneInfo,
) -> datetime.timedelta:
    started_at = started_at.astimezone(timezone)
    return datetime.datetime.now(timezone) - started_at


def humanize_stop_sale_duration(duration: datetime.timedelta) -> str:
    stop_duration_in_seconds = duration.total_seconds()

    if stop_duration_in_seconds >= DAY_IN_SECONDS:
        kwargs = {
            "format": "%0.0f",
            "minimum_unit": "days",
            "suppress": ["months"],
        }
    elif stop_duration_in_seconds >= HOUR_IN_SECONDS:
        kwargs = {"format": "%0.0f", "minimum_unit": "hours"}
    elif stop_duration_in_seconds >= MINUTE_IN_SECONDS:
        kwargs = {"format": "%0.0f", "minimum_unit": "minutes"}
    else:
        kwargs = {"format": "%0.0f", "minimum_unit": "seconds"}

    return abbreviate_time_units(humanize.precisedelta(duration, **kwargs))


class StopSalesBySectorsView(TextView):
    def __init__(self, payload: Iterable[UnitStopSalesBySectors]) -> None:
        self.__units_stop_sales = payload

    @override
    def get_texts(self) -> list[str]:
        since_message = _("render:stop_sales_by_sectors:since")

        result: list[str] = []
        for unit_stop_sales in self.__units_stop_sales:
            timezone = ZoneInfo(unit_stop_sales.timezone)

            lines: list[str] = [
                _("render:stop_sales_by_sectors:title")
                % {"unit_name": unit_stop_sales.unit_name}
            ]
            for stop_sale in unit_stop_sales.stop_sales:
                started_at = parse_datetime(
                    date_string=stop_sale.started_at,
                    timezone=timezone,
                )
                stop_sale_duration = compute_duration(
                    started_at=started_at,
                    timezone=timezone,
                )
                humanized_duration = humanize_stop_sale_duration(stop_sale_duration)

                lines.append(
                    f"{stop_sale.sector_name} - {humanized_duration}"
                    f" ({since_message} {started_at:%H:%M})"
                )

            result.append("\n".join(lines))

        return result
