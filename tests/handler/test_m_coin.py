from src.domain.m_coin import MercadoBitcoinClient


async def test_m_coin_get_quotation():
    coin = 'BTC'
    expected_keys = [
        'high',
        'low',
        'vol',
        'last',
        'buy',
        'sell',
        'date'
    ]

    m_bitcoin = MercadoBitcoinClient()

    quotation = await m_bitcoin.get_quotation(coin)
    for item in expected_keys:
        assert item in quotation.get('ticker')
