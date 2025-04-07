import pathlib
from dataclasses import dataclass
from functools import lru_cache
from typing import Final

import tomllib

ROOT_PATH: Final[pathlib.Path] = pathlib.Path(__file__).parent.parent.parent
CONFIG_FILE_PATH: Final[pathlib.Path] = ROOT_PATH / "config.toml"


@dataclass(frozen=True, slots=True, kw_only=True)
class Config:
    telegram_bot_token: str
    locale_language: str


@lru_cache
def get_config() -> Config:
    config_toml = CONFIG_FILE_PATH.read_text(encoding="utf-8")
    config: dict = tomllib.loads(config_toml)
    return Config(
        telegram_bot_token=config["telegram_bot"]["token"],
        locale_language=config["locale"]["language"],
    )
