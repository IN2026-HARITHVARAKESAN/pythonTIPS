"""Fetch yield updated daily stock prices."""

import asyncio
import aiohttp


API_KEY = "WX10M21VNS7N8WT8"
BASE_URL = "https://www.alphavantage.co/query"

async def fetch_stock_price(session, symbol):
    """Fetch the latest daily price for a stock symbol."""
    params = {
        "function": "TIME_SERIES_DAILY",
        "symbol": symbol,
        "apikey": API_KEY
    }

    async with session.get(BASE_URL, params=params) as response:
        response.raise_for_status()
        data = await response.json()

    if "Error Message" in data:
        raise ValueError(data["Error Message"])

    if "Note" in data or "Information" in data:
        raise RuntimeError(
            data.get("Note") or data.get("Information")
        )

    time_series = data.get("Time Series (Daily)")

    if not time_series:
        raise ValueError(f"No stock data found: {data}")

    latest_date = max(time_series.keys())
    latest_data = time_series[latest_date]

    return {
        "symbol": symbol,
        "date": latest_date,
        "price": float(latest_data["4. close"])
    }

async def stock_price_generator(symbol):
    """Yield changes stock data every five minutes."""
    if not API_KEY:
        raise ValueError("Please set ALPHA_VANTAGE_API_KEY.")

    async with aiohttp.ClientSession() as session:
        previous_data = None

        while True:
            stock_data = await fetch_stock_price(session, symbol)

            if stock_data != previous_data:
                yield stock_data
                previous_data = stock_data

            await asyncio.sleep(300)

async def main():
    """Print stock price."""
    symbol = "IBM"

    async for stock in stock_price_generator(symbol):
        print("Stock:", stock["symbol"])
        print("Date:", stock["date"])
        print("Price:", stock["price"])
        print("------------------------")

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\nStock monitoring stopped.")