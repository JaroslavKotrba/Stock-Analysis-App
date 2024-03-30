# FINANCIAL ANALYSIS

# Libraries
import numpy as np
import pandas as pd
import yfinance as yf
import datetime as dt
from plotly import express as px

### INPUTS

symbol = "MSFT"
period = "5y"
window_mavg_short = 30
window_mavg_long = 90

### DATA

# Stock
stock = yf.Ticker(symbol)

# Attributes
stock_info = stock.info
stock_info

stock_incomestmt = stock.income_stmt
stock_incomestmt

stock_history = stock.history(period=period)
stock_history

### ANALYSIS

# Company information
list(stock_info.keys())

# Assume stock_info is already defined and filled with data
stock_info_keys = list(stock_info.keys())
keys_starting_with_net = [key for key in stock_info_keys if key.startswith("fiscal")]
print(keys_starting_with_net)

# wage
stock_info["companyOfficers"]


# Function to extract the highest paid officer
def get_highest_paid_officer(officers_list):
    highest_paid = max(officers_list, key=lambda officer: officer.get("totalPay", 0))
    return (
        highest_paid["title"],
        highest_paid["name"],
        highest_paid["totalPay"],
    )


title, name, totalPay = get_highest_paid_officer(stock_info["companyOfficers"])

# Company information
stock_info["industry"]
stock_info["fullTimeEmployees"]
stock_info["website"]

# Financial ratios
stock_info["profitMargins"]
stock_info["revenueGrowth"]
# currentRatio > 1 indicates that a company has more current assets than current liabilities (over 1.5 = healthy)
stock_info["currentRatio"]

# Financial operations
stock_info["totalRevenue"]
stock_info["netIncomeToCommon"]
stock_info["operatingCashflow"]

stock_info["ebitda"]
stock_info["marketCap"]
stock_info["enterpriseValue"]

# Stock moving average
stock_df = stock_history[["Close"]].reset_index()
stock_df["mavg_short"] = stock_df["Close"].rolling(window=window_mavg_short).mean()
stock_df["mavg_long"] = stock_df["Close"].rolling(window=window_mavg_long).mean()
stock_df

### VISUALISATION

# Simple
px.line(data_frame=stock_df.set_index("Date"))

# Advance
fig = px.line(
    data_frame=stock_df.set_index("Date"),
    color_discrete_map={
        "Close": "#2C3E50",
        "mavg_short": "#0000FF",
        "mavg_long": "#158cba",
    },
    title="Stock Chart",
)

fig = fig.update_layout(
    plot_bgcolor="rgba(0, 0, 0, 0)",
    paper_bgcolor="rgba(0, 0, 0, 0)",
    legend_title_text="",
)

fig = fig.update_yaxes(title="Share Price", tickprefix="$", gridcolor="#2c3e50")

fig = fig.update_xaxes(title="", gridcolor="#2c3e50")

fig
