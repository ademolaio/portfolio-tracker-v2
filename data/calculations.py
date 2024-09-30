def calculate_market_value(shares, price):
    market_value = shares * price
    return market_value

def calculate_gains_or_losses(market_value, cost_basis):
    gains_or_losses = market_value - cost_basis
    return gains_or_losses