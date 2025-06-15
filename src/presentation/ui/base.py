from abc import ABC, abstractmethod

from aiogram.types import (
    ForceReply,
    InlineKeyboardMarkup,
    ReplyKeyboardMarkup,
    ReplyKeyboardRemove,
)

type ReplyMarkup = (
    InlineKeyboardMarkup | ReplyKeyboardMarkup | ReplyKeyboardRemove | ForceReply
)


class TextView(ABC):
    text: str
    reply_markup: ReplyMarkup | None = None

    @abstractmethod
    def get_texts(self) -> list[str]:
        return [self.text]

    def get_reply_markup(self) -> ReplyMarkup | None:
        return self.reply_markup
