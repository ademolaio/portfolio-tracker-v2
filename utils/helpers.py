import pandas as pd

def format_portfolio_as_dataframe(portfolio_data):
    """
    Converts the portfolio data into a dataframe
    :param portfolio_data:
    :return:
    """
    df = pd.DataFrame(portfolio_data)
    return df