from abc import ABC, abstractmethod

from httpx import AsyncClient


class QuotationCoinsABC(ABC):
    base_url = None

    @abstractmethod
    async def get_quotation(self, coin: str):
        pass

    async def _request(
        self, method: str, resource: str, *args, **kwargs
    ) -> dict:
        url = f'{self.base_url}/{resource}'

        async with AsyncClient() as client:
            response = await client.request(
                method=method, url=url, *args, **kwargs
            )

        response.raise_for_status()

        return response.json()
