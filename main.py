import asyncio
import sys
import json
from .api_client import PrivatBankApiClient
from .currency_rate import CurrencyRateService

async def main():
    if len(sys.argv) != 2:
        print("Usage: python main.py <number_of_days>")
        return

    days = int(sys.argv[1])
    api_client = PrivatBankApiClient()
    currency_rate_service = CurrencyRateService(api_client)

    try:
        # Отримання результатів
        rates = await currency_rate_service.get_currency_rates(days)

        # Перевірка типу даних
        if isinstance(rates, list):
            # Вивід у форматі JSON
            print(json.dumps(rates, ensure_ascii=False, indent=2))
        else:
            print("Error: The result is not a list.")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    asyncio.run(main())