from plotly import express as px


def plotly_chart(stock_history, window_mavg_short=30, window_mavg_long=90):
    """
    Function to create a plotly chart
    """
    stock_df = stock_history[["Close"]].reset_index()

    stock_df["mavg_short"] = stock_df["Close"].rolling(window=window_mavg_short).mean()

    stock_df["mavg_long"] = stock_df["Close"].rolling(window=window_mavg_long).mean()

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

    return fig
