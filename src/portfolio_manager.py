import json
import os

class PortfolioManager:
    def __init__(self, portfolio_file='data/portfolio_data.json'):
        self.portfolio_file = portfolio_file
        self.portfolio = {}
        self.load_portfolio()

