import requests
from utils.config import API_KEY
from utils.exceptions import AlphaVantageAPIError

BASE_URL = 'https://www.alphavantage.co/query'

def fetch_company_overview(ticker):
    """
    Fetch the company overview for a given ticker.
    :param ticker:
    :return:
    """

    params = {
        'function': 'OVERVIEW',
        'symbol': ticker,
        'apikey': API_KEY
    }

    response = requests.get(BASE_URL, params=params)
    if response.status_code != 200:
        raise AlphaVantageAPIError(f"Failed to fetch data for ticker {ticker}: {response.status_code}")

    return response.json()

    if 'Name' not in data:
        raise AlphaVantageAPIError(f"Failed to fetch data for ticker {ticker}")

    return {
        'Name': data.get('Name'),
        'Sector': data.get('Sector'),
        'Industry': data.get('Industry'),
    }
