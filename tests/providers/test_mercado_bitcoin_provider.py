from app.domain.providers import MercadoBitcoinProvider


async def test_get_infos_of_mercado_bitcoin_provider():
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

    m_bitcoin = MercadoBitcoinProvider()

    quotation = await m_bitcoin.get_quotation_client(coin)
    for item in expected_keys:
        assert item in quotation.get('ticker')
