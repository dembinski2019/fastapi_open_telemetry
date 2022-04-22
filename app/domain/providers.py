
from app.domain import QuotationProviderABC
from app.settings import settings
from app.settings.instrumentation import tracer


class MercadoBitcoinProvider(QuotationProviderABC):
    base_url = settings.MERCADO_BITCOIN_URL

    async def get_quotation_client(self, coin):
        with tracer.start_as_current_span(self.get_quotation_client.__name__):
            resource = f'{coin}/ticker'
            resp = await self._request('GET', resource,)
            return resp
