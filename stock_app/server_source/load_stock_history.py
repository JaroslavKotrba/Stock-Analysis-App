import yfinance as yf


def load_stock_history(symbol, period):
    """
    Function to load historical prices per share
    """
    stock = yf.Ticker(symbol)
    stock_history = stock.history(period=period)

    return stock_history
