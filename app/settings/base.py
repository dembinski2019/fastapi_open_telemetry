import os
from typing import Optional

import toml
from pydantic import BaseModel, Field, BaseSettings


class AppSettings(BaseModel):
    """Application settings."""

    PROJECT_NAME: str = None
    PROJECT_VERSION: str = None
    PROJECT_DESCRIPTION: str = None
    BASE_DIR = os.path.dirname(os.path.dirname(
        os.path.dirname(os.path.abspath(__file__))))

    def __init__(self, *args, **kwargs):
        super().__init__()
        with open(os.path.join(self.BASE_DIR, 'pyproject.toml')) as f:
            package_info = toml.load(f)
        self.PROJECT_NAME = package_info['tool']['poetry']['name']
        self.PROJECT_VERSION = package_info['tool']['poetry']['version']
        self.PROJECT_DESCRIPTION = package_info['tool']['poetry']['description']


class GlobalSettings(BaseSettings):

    DEBUG: Optional[bool] = None
    LOG_LEVEL: Optional[str] = Field('info', env='LOG_LEVEL')
    API_PREFIX: Optional[str] = Field('/security', env='API_PREFIX')
    API_STAGE: Optional[str] = Field(None, env='API_STAGE')
    ENVIRONMENT: Optional[str] = Field('', env='ENVIRONMENT')
    ENV_TEST: Optional[bool] = True

    # ============================= PROJECT ==============================
    PROJECT_KEY: Optional[str] = Field(None, env='SECURITY_PROJECT_KEY')
    EXPIRATION_TIME_HOUR: int = 6
    EXPIRATION_REFRESH_TIME_DAY: int = 10
    APP_SETTINGS: AppSettings = AppSettings()

    # ========================= 1rd PARTY APIS ===========================
    MERCADO_BITCOIN_URL: str = Field(env='MERCADO_BITCOIN_URL')
    # ============================= DATABASE =============================
    DATABASE_URL: Optional[str]

    class Config:
        """Loads the dotenv file."""

        env_file: str = os.path.join(AppSettings().BASE_DIR, '.env')
