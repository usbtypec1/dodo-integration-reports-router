from dishka import Provider

from bootstrap.ioc.di_providers.infrastructure.telegram_api import (
    TelegramApiGatewayProvider,
)
from bootstrap.ioc.di_providers.settings import SettingsProvider


def get_providers() -> tuple[Provider, ...]:
    return (
        SettingsProvider(),
        TelegramApiGatewayProvider(),
    )
