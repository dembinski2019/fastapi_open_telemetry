from src.domain.m_coin import MercadoBitcoinClient
from src.schemas.ticker_schemas import TickerSchemas, Coins


class QuotationService():

    async def get_quotation(self, coin: str) -> list[TickerSchemas]:
        quotation_worker = MercadoBitcoinClient()
        results = await quotation_worker.get_quotation(coin)
        coin = Coins[coin]

        return [TickerSchemas(**q.get('ticker'), coin=coin) for q in [results]]
