import gettext
import os

# Указываем путь к папке с переводами
localedir = os.path.join(os.path.dirname(__file__), "locales")
lang = gettext.translation("messages", localedir=localedir, languages=["ru"])
lang.install()

# Теперь _() будет использовать перевод
_ = lang.gettext
