from fastapi import FastAPI
from uvicorn import run

from src.settings import settings
from src.entrypoints.api.routers import router


app = FastAPI(
    debug=settings.DEBUG,
    version=settings.APP_SETTINGS.PROJECT_VERSION,
    title=settings.APP_SETTINGS.PROJECT_NAME,
    description=settings.APP_SETTINGS.PROJECT_DESCRIPTION,
)


app.include_router(router)


def main():
    return run(
        app='src.entrypoints.api.app:app',
        host='0.0.0.0',
        port=8000,
        log_level=settings.LOG_LEVEL,
        debug=settings.DEBUG,
        reload=True if settings.ENVIRONMENT else False,
    )
