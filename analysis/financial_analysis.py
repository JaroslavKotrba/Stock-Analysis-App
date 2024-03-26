# FINANCIAL ANALYSIS

# Libraries
import numpy as np
import pandas as pd
import yfinance as yf
import datetime as dt
from plotly import express as px

# ---------------------------------------------------------------------------------------------------------------
# Inputs --------------------------------------------------------------------------------------------------------

symbol = "MSFT"
period = "5y"
window_navg_short = 30
window_navg_long = 90

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

# wage
stock_info["companyOfficers"]

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
stock_info["ebitda"]
stock_info["operatingCashflow"]

# Stock moving average
stock_df = stock_history[["Close"]].reset_index()
stock_df["mavg_short"] = stock_df["Close"].rolling(window=window_navg_short).mean()
stock_df["mavg_long"] = stock_df["Close"].rolling(window=window_navg_long).mean()
stock_df

### VISUALISATION

# Simple
px.line(data_frame=stock_df.set_index("Date"))

# Advance
fig = px.line(
    data_frame=stock_df.set_index("Date"),
    color_discrete_map={
        "Close": "#2C3E50",
        "mavg_short": "#E31A1C",
        "mavg_long": "#18BC9C",
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
