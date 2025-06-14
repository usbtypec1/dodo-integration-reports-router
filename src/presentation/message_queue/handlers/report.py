import logging

from dishka import FromDishka
from faststream.redis import RedisRouter
from pydantic import BaseModel

from application.interactors.send_message_to_telegram import (
    SendMessageToTelegramInteractor,
)
from infrastructure.adapters.gateways.telegram_api import TelegramApiGateway
from presentation.event_strategies import REPORT_TYPE_ID_TO_RENDERER

log = logging.getLogger(__name__)


router = RedisRouter()


class Event(BaseModel):
    chat_ids: set[int]
    report_type_id: str
    payload: dict | list


@router.subscriber("reports-router")
async def on_report(
    event: Event,
    telegram_api_gateway: FromDishka[TelegramApiGateway],
) -> None:
    try:
        render = REPORT_TYPE_ID_TO_RENDERER[event.report_type_id]
    except KeyError:
        log.error(
            "No renderer found for report type ID: %s",
            event.report_type_id,
        )
    else:
        await SendMessageToTelegramInteractor(
            telegram_api_gateway=telegram_api_gateway,
            chat_ids=event.chat_ids,
            render=render,
            payload=event.payload,
        ).execute()
