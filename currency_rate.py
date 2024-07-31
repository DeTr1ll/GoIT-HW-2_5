from datetime import datetime, timedelta
from .api_client import PrivatBankApiClient

class CurrencyRateService:
    def __init__(self, api_client: PrivatBankApiClient):
        self.api_client = api_client

    async def get_currency_rates(self, days: int):
        if days < 1 or days > 10:
            raise ValueError("Number of days must be between 1 and 10.")
        
        results = []
        for i in range(days):
            date = datetime.today() - timedelta(days=i)
            data = await self.api_client.fetch_exchange_rate(date)
            rates = self._extract_rates(data)
            results.append({date.strftime('%d.%m.%Y'): rates})
        return results

    def _extract_rates(self, data):
        rates = {'EUR': None, 'USD': None}
        for rate in data.get('exchangeRate', []):
            if rate['currency'] in rates:
                rates[rate['currency']] = {
                    'sale': rate['saleRate'],
                    'purchase': rate['purchaseRate']
                }
        return rates