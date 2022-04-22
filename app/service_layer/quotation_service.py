
from app.domain.providers import MercadoBitcoinProvider
from app.schemas.ticker_schemas import TickerSchemas, Coins


class QuotationService():

    async def quotation(self, coin: str) -> list[TickerSchemas]:
        quotation_worker = MercadoBitcoinProvider()
        results = await quotation_worker.get_quotation_client(coin)
        coin = Coins[coin]
        return [TickerSchemas(**q.get('ticker'), coin=coin) for q in [results]]
