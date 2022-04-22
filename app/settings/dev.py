from __future__ import annotations

from .base import GlobalSettings


class DevSettings(GlobalSettings):
    """Development settings."""

    class Config:
        env_prefix: str = 'DEV_'
