from __future__ import annotations

from .base import GlobalSettings


class LocalSettings(GlobalSettings):
    """Local settings."""

    class Config:
        env_prefix: str = 'LOCAL_'
