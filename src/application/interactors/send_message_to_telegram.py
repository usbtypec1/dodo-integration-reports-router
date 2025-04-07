from collections.abc import Callable, Iterable
from dataclasses import dataclass
from typing import Any

from application.ports.gateways.telegram_api import TelegramApiGateway


@dataclass(frozen=True, slots=True, kw_only=True)
class SendMessageToTelegramInteractor:
    render: Callable[..., str]
    chat_ids: Iterable[int]
    telegram_api_gateway: TelegramApiGateway
    payload: Any

    async def execute(self) -> None:
        text = self.render(self.payload)
        for chat_id in self.chat_ids:
            await self.telegram_api_gateway.send_message(
                chat_id=chat_id,
                text=text,
            )
