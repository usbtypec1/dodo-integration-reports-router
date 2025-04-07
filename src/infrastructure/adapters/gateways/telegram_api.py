from dataclasses import dataclass

from aiogram import Bot
from aiogram.enums import ParseMode


@dataclass(frozen=True, slots=True, kw_only=True)
class TelegramApiGateway:
    bot: Bot

    async def send_message(self, *, chat_id: int, text: str) -> None:
        await self.bot.send_message(
            chat_id=chat_id,
            text=text,
            parse_mode=ParseMode.HTML,
        )
