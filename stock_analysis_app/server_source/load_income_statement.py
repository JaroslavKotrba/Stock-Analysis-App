import pandas as pd


def load_income_statement(stock):
    """
    Function to load income statement from Yahoo Finance
    """
    stock_incomestmt = stock.income_stmt
    stock_incomestmt.reset_index(inplace=True)
    stock_incomestmt.rename(columns={"index": "Financial Statement"}, inplace=True)
    # Convert datetime column names to date (string format) without the time part
    stock_incomestmt.columns = stock_incomestmt.columns.map(
        lambda x: x.strftime("%Y-%m-%d") if isinstance(x, pd.Timestamp) else x
    )

    return stock_incomestmt
