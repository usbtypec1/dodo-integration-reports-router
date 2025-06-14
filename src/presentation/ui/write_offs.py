from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from domain.entities.write_offs import WriteOff
from presentation.i18n import gettext as _
from presentation.ui.base import TextView


class WriteOffView(TextView):
    def __init__(self, payload: WriteOff):
        self.__write_off = payload

    def get_text(self) -> str:
        if self.__write_off.is_expired:
            return _("render:write_offs:expired") % {
                "unit_name": self.__write_off.unit_name,
                "ingredient_name": self.__write_off.ingredient_name,
            }

        return _("render:write_offs:expiring") % {
            "unit_name": self.__write_off.unit_name,
            "ingredient_name": self.__write_off.ingredient_name,
            "remaining_minutes": self.__write_off.remaining_minutes,
        }

    def get_reply_markup(self) -> InlineKeyboardMarkup:
        button = InlineKeyboardButton(
            text=_("render:write_offs:button"),
            callback_data=f"write_off:{str(self.__write_off.id)}",
        )
        return InlineKeyboardMarkup(inline_keyboard=[[button]])
