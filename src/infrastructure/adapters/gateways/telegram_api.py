import asyncio
import logging
from dataclasses import dataclass

from aiogram import Bot
from aiogram.enums import ParseMode
from aiogram.exceptions import TelegramAPIError

logger = logging.getLogger(__name__)


@dataclass(frozen=True, slots=True, kw_only=True)
class TelegramApiGateway:
    bot: Bot

    async def send_message(self, *, chat_id: int, text: str) -> None:
        try:
            await self.bot.send_message(
                chat_id=chat_id,
                text=text,
                parse_mode=ParseMode.HTML,
            )
        except TelegramAPIError as error:
            print(error)
            logger.error("Error sending message to chat_id %s", chat_id)
            await asyncio.sleep(1)
