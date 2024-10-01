from data.alpha_vantage_data import fetch_company_overview
from config.columns import COLUMN_HEADERS
from data.ticker_data import securities_dict  # Import the ticker dictionary

def get_portfolio_data():
    """
    Retrieve portfolio data with Alpha Vantage information (Ticker, Name, Sector, Industry).
    Uses dynamic columns for flexibility.
    """
    portfolio_data = []

    for ticker, info in securities_dict.items():
        overview = fetch_company_overview(ticker)
        portfolio_data.append({
            'Ticker': ticker,
            'Name': overview['Name'],
            'Sector': overview['Sector'],
            'Industry': overview['Industry'],
            'Shares': info['shares'],
            'Avg Cost': info['avg_cost']
        })

    return portfolio_data, COLUMN_HEADERS