import humanize.i18n
from faststream import FastStream
from faststream.redis import RedisBroker

from bootstrap.config import get_config
from presentation.message_queue.handlers.report import router


def get_app() -> FastStream:
    config = get_config()
    humanize.i18n.activate(config.locale_language)
    broker = RedisBroker(config.message_queue_url)
    broker.include_router(router)
    app = FastStream(broker)
    return app
