from fastapi import APIRouter, Path
from opentelemetry import trace

from app.schemas.ticker_schemas import TickerSchemas
from app.service_layer.quotation_service import QuotationService


routes = APIRouter()


@routes.get(
    '/{coin}',
    summary='Busca informações das ultimas 24 horas',
    response_model=list[TickerSchemas]
)
async def get_ticker(coin: str = Path(...)):
    span = trace.get_current_span()
    span.add_event(
        'try get tiker',
        attributes={'coin': coin}
    )
    service_worker = QuotationService()
    info_coins = await service_worker.quotation(coin=coin)

    return info_coins
