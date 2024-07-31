import aiohttp
from datetime import datetime
from .exceptions import ApiException

class PrivatBankApiClient:
    BASE_URL = 'https://api.privatbank.ua/p24api/exchange_rates?json&date='

    async def fetch_exchange_rate(self, date: datetime):
        formatted_date = date.strftime('%d.%m.%Y')
        url = f"{self.BASE_URL}{formatted_date}"
        async with aiohttp.ClientSession() as session:
            try:
                async with session.get(url) as response:
                    if response.status != 200:
                        raise ApiException(f"Error fetching data: {response.status}")
                    return await response.json()
            except aiohttp.ClientError as e:
                raise ApiException(f"Network error: {e}")