from fastapi import FastAPI
from uvicorn import run
from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor
from app.settings import settings
from app.entrypoints.api.routers import router
from .exception_handlers import exception_handlers


app = FastAPI(
    debug=settings.DEBUG,
    version=settings.APP_SETTINGS.PROJECT_VERSION,
    title=settings.APP_SETTINGS.PROJECT_NAME,
    description=settings.APP_SETTINGS.PROJECT_DESCRIPTION,
)


FastAPIInstrumentor.instrument_app(app)


def register_errors_handler(app: FastAPI):
    for exception, handler in exception_handlers.items():
        app.add_exception_handler(exception, handler)


app.include_router(router)

register_errors_handler(app)


def main():
    return run(
        app='app.entrypoints.api.app:app',
        host='0.0.0.0',
        port=8000,
        log_level=settings.LOG_LEVEL,
        debug=settings.DEBUG,
        reload=True if settings.ENVIRONMENT else False,
    )
