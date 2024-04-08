from plotly import express as px
from server_source.prophet_forecast import prophet_forecast


def plotly_chart(stock_history, window_mavg_short=30, window_mavg_long=90):
    """
    Function to create a plotly chart
    """
    stock_df = stock_history[["Close"]].reset_index()
    stock_df = stock_df.rename(columns={"Date": "date"})
    stock_df = stock_df.rename(columns={"Close": "closing_price"})

    # Moving average short
    stock_df["mavg_short"] = (
        stock_df["closing_price"].rolling(window=window_mavg_short).mean()
    )

    # Moving average long
    stock_df["mavg_long"] = (
        stock_df["closing_price"].rolling(window=window_mavg_long).mean()
    )

    # Forecasting
    future_forecast, start_date = prophet_forecast(stock_df)

    # Main lines
    fig = px.line(
        data_frame=stock_df.set_index("date"),
        # template="simple_white",
        color_discrete_map={
            "closing_price": "#2C3E50",
            "mavg_short": "#0000FF",
            "mavg_long": "#158cba",
        },
        # title="Stock Chart",
    )

    # Forecasting
    fig.add_scatter(
        x=future_forecast["ds"],
        y=future_forecast["yhat"],
        mode="lines",
        name="forecast",
        line=dict(color="#4191E1", dash="dot"),
        hovertemplate="variable=forecast<br>"
        + "date=%{x}<br>"
        + "value=%{y:$,.2f}<br>"
        + "<extra></extra>",  # This hides the trace name in the tooltip
    )

    # Add vertical line to separate forecasting
    fig.add_vline(
        x=start_date,
        line=dict(color="black", width=2, dash="dashdot"),
        line_width=2,
    )

    # Add range buttons
    fig.update_layout(
        xaxis=dict(
            rangeselector=dict(
                buttons=list(
                    [
                        dict(count=1, label="1m", step="month", stepmode="backward"),
                        dict(count=6, label="6m", step="month", stepmode="backward"),
                        dict(count=1, label="YTD", step="year", stepmode="todate"),
                        dict(count=1, label="1y", step="year", stepmode="backward"),
                        dict(count=3, label="3y", step="year", stepmode="backward"),
                        dict(count=5, label="5y", step="year", stepmode="backward"),
                        dict(step="all", label="All"),
                    ]
                )
            ),
            type="date",
        )
    )

    # Background
    fig = fig.update_layout(
        plot_bgcolor="rgba(0, 0, 0, 0)",
        # paper_bgcolor="rgba(0, 0, 0, 0)",
        legend_title_text="",
    )

    fig = fig.update_yaxes(title="Share Price", tickprefix="$", gridcolor="#2c3e50")

    fig = fig.update_xaxes(title="", gridcolor="#2c3e50")

    return fig
