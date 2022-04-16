from __future__ import annotations

from .base import GlobalSettings


class ProdSettings(GlobalSettings):
    """Production settings."""

    class Config:
        env_prefix: str = 'PROD_'
