from fast_depends import inject
from faststream.redis import RedisRouter
from pydantic import BaseModel

from application.interactors.send_message_to_telegram import (
    SendMessageToTelegramInteractor,
)
from presentation.dependencies.gateways import TelegramApiGatewayProvider
from presentation.event_strategies import REPORT_TYPE_ID_TO_RENDERER

router = RedisRouter()


class Event(BaseModel):
    chat_ids: set[int]
    report_type_id: str
    payload: dict | list


@router.subscriber("reports")
@inject
async def on_report(
    event: Event,
    telegram_api_gateway: TelegramApiGatewayProvider,
) -> None:
    try:
        render = REPORT_TYPE_ID_TO_RENDERER[event.report_type_id]
    except KeyError:
        return

    await SendMessageToTelegramInteractor(
        telegram_api_gateway=telegram_api_gateway,
        chat_ids=event.chat_ids,
        render=render,
        payload=event.payload,
    ).execute()
