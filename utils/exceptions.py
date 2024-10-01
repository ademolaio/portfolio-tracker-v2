class AlphaVantageAPIError(Exception):
    """
    Exception raised when there is an issue with fetching data from Alpha Vantage.
    """
    def __init__(self, message="Error fetching data from Alpha Vantage API"):
        self.message = message
        super().__init__(self.message)