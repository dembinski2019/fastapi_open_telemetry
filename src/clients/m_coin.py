

from src.settings import settings
from src.clients import QuotationCoinsABC


class MercadoBitcoinClient(QuotationCoinsABC):
    base_url = settings.MERCADO_BITCOIN_URL

    async def get_quotation(self, coin):

        resource = f'{coin}/ticker'

        resp = await self._request('GET', resource,)

        return resp
