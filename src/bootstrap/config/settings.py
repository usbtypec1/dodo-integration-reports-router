import pathlib
from typing import Final, Self

import tomllib
from pydantic import BaseModel

ROOT_PATH: Final[pathlib.Path] = pathlib.Path(__file__).parent.parent.parent
CONFIG_FILE_PATH: Final[pathlib.Path] = ROOT_PATH / "config.toml"


class TelegramBotSettings(BaseModel):
    token: str


class MessageQueueSettings(BaseModel):
    url: str


class Settings(BaseModel):
    telegram_bot: TelegramBotSettings
    locale_language: str
    message_queue: MessageQueueSettings

    @classmethod
    def from_toml(cls) -> Self:
        config_toml = CONFIG_FILE_PATH.read_text(encoding="utf-8")
        config: dict = tomllib.loads(config_toml)
        return cls.model_validate(config)
