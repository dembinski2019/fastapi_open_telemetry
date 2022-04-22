from typing import Callable

from fastapi import Request
from fastapi.responses import JSONResponse


from app.exceptions.providers_exceptions import APIException, CoinNotFound


def http_exception_factory(status_code: int) -> Callable:
    def http_exception(_: Request, exception: APIException) -> JSONResponse:
        return JSONResponse(
            status_code=status_code,
            content={'message': exception.message}
        )

    return http_exception


exception_handlers = {
    CoinNotFound: http_exception_factory(404)
}
