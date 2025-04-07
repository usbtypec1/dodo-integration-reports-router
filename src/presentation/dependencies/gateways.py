from collections.abc import AsyncGenerator
from typing import Annotated

from aiogram import Bot
from fast_depends import Depends

from infrastructure.adapters.gateways.telegram_api import TelegramApiGateway
from presentation.dependencies.config import ConfigProvider


async def telegram_api_gateway_provider(
    config: ConfigProvider,
) -> AsyncGenerator[TelegramApiGateway, None]:
    async with Bot(token=config.telegram_bot_token) as bot:
        yield TelegramApiGateway(bot=bot)


TelegramApiGatewayProvider = Annotated[
    TelegramApiGateway,
    Depends(telegram_api_gateway_provider),
]
