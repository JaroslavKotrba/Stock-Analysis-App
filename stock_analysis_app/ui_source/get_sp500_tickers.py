import pandas as pd


def get_sp500_tickers():
    """
    Function to get S&P500 tickers
    """
    table = pd.read_html("https://en.wikipedia.org/wiki/List_of_S%26P_500_companies")
    sp500_df = table[0]
    sp500_df["Symbol"] = sp500_df["Symbol"].str.replace(".", "-")
    sp500_df["Ticker-Name"] = (
        sp500_df["Symbol"].astype(str) + " | " + sp500_df["Security"].astype(str)
    )

    return sp500_df["Ticker-Name"].tolist()
