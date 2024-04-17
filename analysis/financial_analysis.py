# FINANCIAL ANALYSIS

# Libraries
import numpy as np
import pandas as pd
import pandas_datareader as pdr
import yfinance as yf
import datetime as dt
from plotly import express as px
import plotly.graph_objects as go
from prophet import Prophet

### INPUTS

symbol = "MSFT"  # "^GSPC"
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
stock_incomestmt.reset_index(inplace=True)
stock_incomestmt.rename(columns={"index": "Financial Statement"}, inplace=True)
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
stock_df = stock_df.rename(columns={"Date": "date"})
stock_df = stock_df.rename(columns={"Close": "closing_price"})

stock_df["mavg_short"] = (
    stock_df["closing_price"].rolling(window=window_mavg_short).mean()
)

stock_df["mavg_long"] = (
    stock_df["closing_price"].rolling(window=window_mavg_long).mean()
)
stock_df

# Forecast
prophet_df = stock_df[["date", "closing_price"]].rename(
    columns={"date": "ds", "closing_price": "y"}
)

prophet_df["ds"] = prophet_df["ds"].dt.tz_localize(None)

start_date = prophet_df["ds"].max() + pd.Timedelta(days=1)
cutoff_date = prophet_df["ds"].max() - pd.DateOffset(years=1)

model = Prophet()
model.fit(prophet_df[prophet_df["ds"] > cutoff_date])

future = model.make_future_dataframe(periods=120)

forecast = model.predict(future)

future_forecast = forecast[forecast["ds"] >= pd.to_datetime(start_date)][["ds", "yhat"]]

### VISUALISATION

# SIMPLE
px.line(data_frame=stock_df.set_index("date"))

# ADVANCE
fig = go.Figure()

# Lines
fig.add_trace(
    go.Scatter(
        x=stock_df["date"],
        y=stock_df["closing_price"],
        mode="lines",
        name="CP",
        line=dict(color="#2C3E50"),
        hovertemplate="Closing Price (%{x}, $%{y:.2f})<extra></extra>",
    )
)
fig.add_trace(
    go.Scatter(
        x=stock_df["date"],
        y=stock_df["mavg_short"],
        mode="lines",
        name="SMA",
        line=dict(color="#0000FF"),
        hovertemplate="Short Moving Average (%{x}, $%{y:.2f})<extra></extra>",
    )
)
fig.add_trace(
    go.Scatter(
        x=stock_df["date"],
        y=stock_df["mavg_long"],
        mode="lines",
        name="LMA",
        line=dict(color="#158cba"),
        hovertemplate="Long Moving Average (%{x}, $%{y:.2f})<extra></extra>",
    )
)

fig.add_trace(
    go.Scatter(
        x=future_forecast["ds"],
        y=future_forecast["yhat"],
        mode="lines",
        name="Forecast",
        line=dict(color="#4191E1", dash="dot"),
        hovertemplate="Forecast (%{x}, $%{y:.2f})<extra></extra>",
    )
)

# Add vertical line to separate past data from forecast
fig.add_vline(x=start_date, line=dict(color="black", width=2, dash="dashdot"))

# Configure range buttons for x-axis
fig.update_layout(
    xaxis=dict(
        rangeselector=dict(
            buttons=[
                dict(count=1, label="YTD", step="year", stepmode="todate"),
                dict(count=3, label="3y", step="year", stepmode="backward"),
                dict(count=5, label="5y", step="year", stepmode="backward"),
                dict(step="all", label="All"),
            ],
            font=dict(color="white"),  # text color of the buttons
            bgcolor="#555",  # background color of the buttons
            activecolor="#158cba",  # background color of the active button
            x=-0.1,  # position x
            y=-0.15,  # position y
        ),
        type="date",
        gridcolor="#2c3e50",
    )
)

# Update y-axis properties
fig.update_yaxes(title="Share Price", tickprefix="$", gridcolor="#2c3e50")

# Update figure's layout for better appearance
fig.update_layout(
    plot_bgcolor="rgba(0, 0, 0, 0)",
    showlegend=True,
    legend_title_text="",
    # modebar={'displayModeBar': False}  # This line disables the modebar
)

# fig.update_layout(config={'displayModeBar': False})

fig.show(config={"displayModeBar": False})

### TICKERS


def get_sp500_tickers():
    table = pd.read_html("https://en.wikipedia.org/wiki/List_of_S%26P_500_companies")
    sp500_df = table[0]
    sp500_df["Symbol"] = sp500_df["Symbol"].str.replace(".", "-")
    sp500_df["Ticker-Name"] = (
        sp500_df["Symbol"].astype(str) + " | " + sp500_df["Security"].astype(str)
    )

    return sp500_df["Ticker-Name"].tolist()


# Example usage
stock = get_sp500_tickers()

### DCF CALCULATION
# https://www.youtube.com/watch?v=Vi-BQx4gE3k
