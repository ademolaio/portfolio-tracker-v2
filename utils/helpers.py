import pandas as pd

def format_portfolio_as_dataframe(portfolio_data):
    """
    Convert portfolio data to a pandas DataFrame for easier display.
    """
    df = pd.DataFrame(portfolio_data)
    return df