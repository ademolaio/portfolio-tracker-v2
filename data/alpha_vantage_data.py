import requests
from utils.config import API_KEY
from utils.exceptions import AlphaVantageAPIError

BASE_URL = 'https://www.alphavantage.co/query'


def fetch_company_overview(ticker):
    """
    Fetch the company overview information like Name, Sector, and Industry from Alpha Vantage API.
    """
    params = {
        'function': 'OVERVIEW',
        'symbol': ticker,
        'apikey': API_KEY
    }
    response = requests.get(BASE_URL, params=params)

    if response.status_code != 200:
        raise AlphaVantageAPIError(f"Failed to fetch data for {ticker}: {response.status_code}")

    data = response.json()

    if 'Name' not in data:
        raise AlphaVantageAPIError(f"Invalid data returned for {ticker}")

    return {
        'Name': data.get('Name'),
        'Sector': data.get('Sector'),
        'Industry': data.get('Industry')
    }