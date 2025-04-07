from typing import Protocol


class TelegramApiGateway(Protocol):
    async def send_message(self, *, chat_id: int, text: str): ...
