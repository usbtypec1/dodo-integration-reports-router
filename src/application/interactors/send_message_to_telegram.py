from collections.abc import Callable, Iterable
from dataclasses import dataclass

from application.ports.gateways.telegram_api import TelegramApiGateway


@dataclass(frozen=True, slots=True, kw_only=True)
class SendMessageToTelegramInteractor[T]:
    render: Callable[[T], str]
    parser: Callable[..., T]
    chat_ids: Iterable[int]
    telegram_api_gateway: TelegramApiGateway

    async def execute(self) -> None:
        text = self.render(self.parser())
        for chat_id in self.chat_ids:
            await self.telegram_api_gateway.send_message(
                chat_id=chat_id,
                text=text,
            )
