# mutual_funds/tasks.py
from celery import shared_task
import requests

# API Key provided by you
API_KEY = 'L5EJBHKBH584U5XH'

# Base URL for Alpha Vantage API
BASE_URL = 'https://www.alphavantage.co/query'

@shared_task
def analyze_fund(symbol):
    try:
        # Fetch stock data
        stock_data = fetch_stock_data(symbol)
        return {'status': 'success', 'stock_data': stock_data}
    except Exception as e:
        return {'status': 'failed', 'error': str(e)}

def fetch_stock_data(symbol):
    """
    Function to fetch stock data for the given symbol from Alpha Vantage API
    """
    # Prepare the API request parameters
    params = {
        'function': 'TIME_SERIES_DAILY',  # Daily stock data
        'symbol': symbol,
        'apikey': API_KEY  # Your API key for Alpha Vantage
    }

    # Send the request to the Alpha Vantage API
    response = requests.get(BASE_URL, params=params)

    # Check if the response is successful
    if response.status_code != 200:
        raise Exception("Failed to fetch data from Alpha Vantage API")

    # Parse the response as JSON
    data = response.json()

    # Ensure that the expected data is present in the response
    if 'Time Series (Daily)' not in data:
        raise Exception("Invalid response or symbol not found")

    # Get the time series data
    time_series = data['Time Series (Daily)']
    latest_date = next(iter(time_series))  # Get the most recent date from the time series
    latest_data = time_series[latest_date]

    # Return the data for the latest date (Open, Close, High, Low, Volume)
    return {
        'Open': latest_data['1. open'],
        'Close': latest_data['4. close'],
        'High': latest_data['2. high'],
        'Low': latest_data['3. low'],
        'Volume': latest_data['5. volume']
    }
