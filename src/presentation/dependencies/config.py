from typing import Annotated

from fast_depends import Depends

from bootstrap.config import Config, get_config


def config_provider() -> Config:
    return get_config()


ConfigProvider = Annotated[Config, Depends(config_provider)]
