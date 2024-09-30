class AlphaVantageAPIError(Exception):
    """
    Exception raised when an error occurs during the AlphaVantage API call.
    """
    def __init__(self, message="Error fetching data from AlphaVantage API"):
        self.message = message
        super().__init__(self.message)