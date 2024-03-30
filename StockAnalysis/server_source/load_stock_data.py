import yfinance as yf


def load_stock_data(symbol):
    """
    Function to load information data from Yahoo Finance
    """
    stock = yf.Ticker(symbol)
    stock_info = stock.info

    return stock_info
