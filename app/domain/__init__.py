from abc import ABC, abstractmethod

from httpx import AsyncClient, AsyncHTTPTransport
from opentelemetry.instrumentation.httpx import AsyncOpenTelemetryTransport

from app.exceptions.providers_exceptions import CoinNotFound


class QuotationProviderABC(ABC):
    base_url = None

    @abstractmethod
    async def get_quotation_client(self, coin: str):
        pass

    async def _request(
        self, method: str, resource: str, *args, **kwargs
    ) -> dict:
        url = f'{self.base_url}/{resource}'
        transport = AsyncHTTPTransport()
        telemetry_transport = AsyncOpenTelemetryTransport(transport)
        async with AsyncClient(transport=telemetry_transport) as client:
            response = await client.request(
                method=method, url=url, *args, **kwargs
            )

        if response.status_code >= 400:
            raise CoinNotFound

        return response.json()
