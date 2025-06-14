from dishka import Provider, Scope, from_context, provide

from bootstrap.config.settings import Settings
from infrastructure.types import MessageQueueUrl, TelegramBotToken
from presentation.types import LocaleLanguage


class SettingsProvider(Provider):
    scope = Scope.APP

    settings = from_context(provides=Settings)

    @provide
    def provide_telegram_settings(self, settings: Settings) -> TelegramBotToken:
        return TelegramBotToken(settings.telegram_bot.token)

    @provide
    def provide_locale_language(self, settings: Settings) -> LocaleLanguage:
        return LocaleLanguage(settings.locale_language)

    @provide
    def provide_message_queue_url(self, settings: Settings) -> MessageQueueUrl:
        return MessageQueueUrl(settings.message_queue.url)
