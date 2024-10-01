def calculate_market_value(shares, price):
    """
    Calculate the market value by multiplying shares with current price.
    """
    return shares * price

def calculate_gains_or_losses(market_value, cost_basis):
    """
    Calculate gains or losses based on the market value and cost basis.
    """
    return market_value - cost_basis