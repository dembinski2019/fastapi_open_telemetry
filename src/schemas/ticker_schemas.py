from decimal import Decimal
from datetime import date
from pydantic import BaseModel


class TickerSchemas(BaseModel):
    high: Decimal
    low: Decimal
    vol: Decimal
    last: Decimal
    buy: Decimal
    sell: Decimal
    date: date
