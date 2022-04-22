from fastapi import APIRouter
from . import quotation

router = APIRouter()

router.include_router(quotation.routes)
