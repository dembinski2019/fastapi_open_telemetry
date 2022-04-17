from fastapi import APIRouter, Path
from src.schemas.ticker_schemas import TickerSchemas
from src.service_layer.coin_quotation import QuotationService


routes = APIRouter()


@routes.get(
    '/{coin}',
    summary='Busca informações das ultimas 24 horas',
    response_model=list[TickerSchemas]
)
async def get_ticker(coin: str = Path(...)):
    service_worker = QuotationService()
    info_coins = await service_worker.get_quotation(coin=coin)

    return info_coins
