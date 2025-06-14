from aiogram import Bot
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from dishka import FromDishka, Provider, Scope, provide

from infrastructure.adapters.gateways.telegram_api import TelegramApiGateway
from infrastructure.types import TelegramBotToken


class TelegramApiGatewayProvider(Provider):
    scope = Scope.APP

    @provide
    def provide_bot(
        self,
        telegram_bot_token: FromDishka[TelegramBotToken],
    ) -> Bot:
        return Bot(
            token=telegram_bot_token,
            default=DefaultBotProperties(parse_mode=ParseMode.HTML),
        )

    @provide
    def provide_telegram_api_gateway(
        self,
        bot: Bot,
    ) -> TelegramApiGateway:
        return TelegramApiGateway(bot=bot)
