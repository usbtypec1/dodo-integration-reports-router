from abc import abstractmethod
from typing import Protocol

from presentation.ui.base import ReplyMarkup


class TelegramApiGateway(Protocol):
    @abstractmethod
    async def send_message(
        self,
        *,
        chat_id: int,
        text: str,
        reply_markup: ReplyMarkup | None = None,
    ): ...
