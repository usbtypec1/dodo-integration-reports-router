import humanize.i18n
from dishka import make_async_container
from dishka.integrations.faststream import FastStreamProvider, setup_dishka
from faststream import FastStream
from faststream.redis import RedisBroker

from bootstrap.config.settings import Settings
from bootstrap.ioc.registry import get_providers
from presentation.message_queue.handlers.report import router


def get_app() -> FastStream:
    settings = Settings.from_toml()

    container = make_async_container(
        *get_providers(),
        FastStreamProvider(),
        context={Settings: settings},
    )

    humanize.i18n.activate(settings.locale_language)

    broker = RedisBroker()
    broker.include_router(router)
    app = FastStream(broker)
    setup_dishka(container=container, app=app, auto_inject=True)
    return app
