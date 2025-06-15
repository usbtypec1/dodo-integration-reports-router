import logging

from dishka import FromDishka
from faststream.redis import RedisRouter
from pydantic import BaseModel, ValidationError

from application.interactors.send_message_to_telegram import (
    SendMessageToTelegramInteractor,
)
from infrastructure.adapters.gateways.telegram_api import TelegramApiGateway
from presentation.event_strategies import (
    REPORT_TYPE_ID_TO_RENDERER_AND_PYDANTIC_MODEL,
    parse_payload,
)

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
        view_class, pydantic_model = REPORT_TYPE_ID_TO_RENDERER_AND_PYDANTIC_MODEL[
            event.report_type_id
        ]
    except KeyError:
        log.error(
            "No renderer found for report type ID: %s",
            event.report_type_id,
        )
        return

    try:
        payload = parse_payload(event.payload, pydantic_model)
    except ValidationError as error:
        log.error(
            "Failed to parse payload for report type ID %s: %s",
            event.report_type_id,
            error,
        )
        return

    view = view_class(payload)

    await SendMessageToTelegramInteractor(
        telegram_api_gateway=telegram_api_gateway,
        chat_ids=event.chat_ids,
        view=view,
        payload=payload,
    ).execute()
