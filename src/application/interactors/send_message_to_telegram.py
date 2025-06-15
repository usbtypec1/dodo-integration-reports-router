from collections.abc import Iterable
from dataclasses import dataclass
from typing import Any

from application.ports.gateways.telegram_api import TelegramApiGateway
from presentation.event_strategies import ReportView


@dataclass(frozen=True, slots=True, kw_only=True)
class SendMessageToTelegramInteractor:
    view: ReportView
    chat_ids: Iterable[int]
    telegram_api_gateway: TelegramApiGateway
    payload: Any

    async def execute(self) -> None:
        texts = self.view.get_texts()
        for text in texts:
            for chat_id in self.chat_ids:
                await self.telegram_api_gateway.send_message(
                    chat_id=chat_id,
                    text=text,
                )
