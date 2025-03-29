import requests

# Function to fetch real-time mutual fund data from Alpha Vantage API
def fetch_real_time_data(symbol):
    api_key = 'L5EJBHKBH584U5XH'  # Replace with your actual API key
    base_url = 'https://www.alphavantage.co/query'

    # Endpoint for daily time series data (or other relevant endpoint for mutual funds)
    url = f"{base_url}?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={api_key}"

    response = requests.get(url)
    data = response.json()

    if 'Time Series (Daily)' in data:
        return data['Time Series (Daily)']
    else:
        return None
