from typing import Optional

from pydantic import BaseSettings
from .base import GlobalSettings
from .dev import DevSettings
from .local import LocalSettings
from .prod import ProdSettings
from .test import TestSettings


class FactorySettings:
    def __init__(self, environment: Optional[str]) -> BaseSettings:
        self.environment = environment

    def __call__(self):
        env_options = {
            'local': LocalSettings,
            'dev': DevSettings,
            'prod': ProdSettings,
            'test': TestSettings,
        }
        settings = env_options.get(self.environment, TestSettings)()
        return settings


settings = FactorySettings(GlobalSettings().ENVIRONMENT)()
