import asyncio
import logging
from dataclasses import dataclass

from aiogram import Bot
from aiogram.enums import ParseMode
from aiogram.exceptions import (
    TelegramAPIError,
    TelegramNetworkError,
    TelegramRetryAfter,
    TelegramServerError,
)

logger = logging.getLogger(__name__)


@dataclass(frozen=True, slots=True, kw_only=True)
class TelegramApiGateway:
    bot: Bot

    async def send_message(
        self,
        *,
        chat_id: int,
        text: str,
        attempts: int = 10,
    ) -> None:
        for attempt in range(attempts):
            try:
                await self.bot.send_message(
                    chat_id=chat_id,
                    text=text,
                    parse_mode=ParseMode.HTML,
                )
            except (
                TelegramRetryAfter,
                TelegramNetworkError,
                TelegramServerError,
            ) as error:
                logger.warning(
                    "Retrying to send message to chat_id %s after error: %s. Attempt %d/%d",
                    chat_id,
                    error,
                    attempt + 1,
                    attempts,
                )
                await asyncio.sleep(5)
            except TelegramAPIError as error:
                logger.error(
                    "Error sending message to chat_id %s error %s",
                    chat_id,
                    error,
                )
                break
            finally:
                await asyncio.sleep(1)
