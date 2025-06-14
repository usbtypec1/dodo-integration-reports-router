import asyncio
import logging
from dataclasses import dataclass
from typing import override

from aiogram import Bot
from aiogram.enums import ParseMode
from aiogram.exceptions import (
    TelegramAPIError,
    TelegramNetworkError,
    TelegramRetryAfter,
    TelegramServerError,
)

from application.ports.gateways.telegram_api import (
    TelegramApiGateway as ITelegramApiGateway,
)
from presentation.ui.base import ReplyMarkup

logger = logging.getLogger(__name__)


@dataclass(frozen=True, slots=True, kw_only=True)
class TelegramApiGateway(ITelegramApiGateway):
    bot: Bot

    @override
    async def send_message(
        self,
        *,
        chat_id: int,
        text: str,
        reply_markup: ReplyMarkup | None = None,
        attempts: int = 10,
    ) -> None:
        for attempt in range(attempts):
            try:
                await self.bot.send_message(
                    chat_id=chat_id,
                    text=text,
                    parse_mode=ParseMode.HTML,
                    reply_markup=reply_markup,
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
