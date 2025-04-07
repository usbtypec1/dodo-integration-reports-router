import gettext

from bootstrap.config import ROOT_PATH, get_config

localedir = ROOT_PATH / "locales"
lang = gettext.translation(
    "messages",
    localedir=localedir,
    languages=[get_config().locale_language],
)
lang.install()

gettext = lang.gettext
