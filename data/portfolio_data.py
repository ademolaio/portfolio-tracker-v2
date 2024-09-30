from sys import int_info

from data.alpha_vantage_data import fetch_company_overview
from config.columns import COLUMN_HEADERS
from data.ticker_data import securities_dict

def get_portfolio_data():
    """
    Retrieve portfolio data from Alpha Vantage Inforamtion (Ticker, Name, Sector, Industry).
    Users dynamic columns for flexibility
    :return:
    """

    portfolio_data = []

    for ticker, info in securities_dict.items():
        overview = fetch_company_overview(ticker)
        portfolio_data.append({
            'Ticker': ticker,
            'Name': overview.get('Name', 'Unknown'),
            'Sector': overview.get('Sector', 'Unknown'),
            'Industry': overview.get('Industry', 'Unknown'),
            'Shares': info['shares'],
            'Avg Cost':info['avg_cost']
        })

        return portfolio_data, COLUMN_HEADERS