from __future__ import annotations

from .base import GlobalSettings


class TestSettings(GlobalSettings):
    """Test settings."""

    class Config:
        env_prefix: str = 'TEST_'
