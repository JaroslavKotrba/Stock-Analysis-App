import plotly.graph_objects as go
from server_source.prophet_forecast import prophet_forecast


def plotly_chart(stock_history, months, window_mavg_short=30, window_mavg_long=90):
    """
    Function to create a Plotly chart using Graph Objects
    """
    stock_df = stock_history[["Close"]].reset_index()
    stock_df = stock_df.rename(columns={"Date": "date", "Close": "closing_price"})

    # Moving averages
    stock_df["mavg_short"] = (
        stock_df["closing_price"].rolling(window=window_mavg_short).mean()
    )
    stock_df["mavg_long"] = (
        stock_df["closing_price"].rolling(window=window_mavg_long).mean()
    )

    # Forecasting
    future_forecast, start_date = prophet_forecast(
        stock_df, months, train=3
    )  # trained on 3 years by default

    fig = go.Figure()

    # Lines
    fig.add_trace(
        go.Scatter(
            x=stock_df["date"],
            y=stock_df["closing_price"],
            mode="lines",
            name="CP",
            line=dict(color="#008000"),
            fill="tozeroy",  # Fill to zero on the y-axis
            fillcolor="rgba(0, 128, 0, 0.5)",  # Green color with 50% transparency
            hovertemplate="Closing Price (%{x}, $%{y:,.2f})",
        )
    )

    fig.add_trace(
        go.Scatter(
            x=stock_df["date"],
            y=stock_df["mavg_short"],
            mode="lines",
            name="SMA",
            line=dict(color="#0000FF"),
            hovertemplate="Short Moving Average (%{x}, $%{y:,.2f})",
        )
    )

    fig.add_trace(
        go.Scatter(
            x=stock_df["date"],
            y=stock_df["mavg_long"],
            mode="lines",
            name="LMA",
            line=dict(color="#158cba"),
            hovertemplate="Long Moving Average (%{x}, $%{y:,.2f})",
        )
    )

    fig.add_trace(
        go.Scatter(
            x=future_forecast["ds"],
            y=future_forecast["yhat"],
            mode="lines",
            name="Fc",
            line=dict(color="#4191E1", dash="dot"),
            fill="tozeroy",  # Fill to zero on the y-axis
            fillcolor="rgba(65, 145, 225, 0.5)",  # Blue color with 50% transparency
            hovertemplate="Forecast (%{x}, $%{y:,.2f})",
        )
    )

    # Add vertical line to separate past data from forecast
    fig.add_vline(x=start_date, line=dict(color="black", width=2, dash="dashdot"))

    # 0 y line
    fig.add_hline(
        y=0,
        line=dict(color="#2c3e50", width=1),
    )

    # Configure range buttons for x-axis
    fig.update_layout(
        xaxis=dict(
            rangeselector=dict(
                buttons=[
                    dict(count=1, label="YTD", step="year", stepmode="todate"),
                    # dict(count=1, label="1y", step="year", stepmode="backward"),
                    dict(count=3, label="3y", step="year", stepmode="backward"),
                    dict(count=5, label="5y", step="year", stepmode="backward"),
                    dict(step="all", label="All"),
                ],
                font=dict(color="white"),  # text color of the buttons
                bgcolor="#555",  # background color of the buttons
                activecolor="#158cba",  # background color of the active button
                x=-0.1,  # position x
                y=-0.3,  # position y
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

    return fig