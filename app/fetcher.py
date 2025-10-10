# app/fetcher.py
from app.postgres_writer import save_market_data_to_postgres
from app.cache import get_cached_data, set_cached_data
import aiohttp
import asyncio
from app.models import MarketSymbol
from datetime import datetime, time
from app.postgres_reader import read_market_data_from_postgres

def is_market_open() -> bool:
    now = datetime.now()
    # Optional: skip weekends (Saturday to Wednesday are workdays in Iran)
    if now.weekday() >= 5:  # 5 = Friday, 6 = Saturday
        return False
    return time(9, 0) <= now.time() <= time(12, 30)



URL = "https://cdn.tsetmc.com/api/ClosingPrice/GetMarketWatch?market=0&industrialGroup=&paperTypes%5B0%5D=1&paperTypes%5B1%5D=2&paperTypes%5B2%5D=3&paperTypes%5B3%5D=4&paperTypes%5B4%5D=5&paperTypes%5B5%5D=6&paperTypes%5B6%5D=7&paperTypes%5B7%5D=8&paperTypes%5B8%5D=9&showTraded=false&withBestLimits=true&hEven=0&RefID=0"

CACHE_KEY = "market_data"

async def fetch_market_data():
    cached = get_cached_data(CACHE_KEY)
    if cached:
        print("Using cached data...")
        return [MarketSymbol(**item) for item in cached]

    db_data = read_market_data_from_postgres()
    if len(db_data)<1:
        async with aiohttp.ClientSession() as session:
            async with session.get(URL) as response:
                print('filling db for first time!')
                raw = await response.json()
                data = raw["marketwatch"]
                models = [MarketSymbol(**item) for item in data]
                save_market_data_to_postgres(models)

    if not is_market_open():
        print("Market closed — reading from DB...")
        return read_market_data_from_postgres()
    
    async with aiohttp.ClientSession() as session:
        async with session.get(URL) as response:
            print('Requesting...')
            raw = await response.json()
            data = raw["marketwatch"]
            models = [MarketSymbol(**item) for item in data]
            set_cached_data(CACHE_KEY, data)
            save_market_data_to_postgres(models)
            return models

if __name__ == "__main__":
    asyncio.run(fetch_market_data())



