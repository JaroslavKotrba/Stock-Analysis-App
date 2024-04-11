import pandas as pd
from prophet import Prophet


def prophet_forecast(stock_df):
    """
    Function to create forecasting model
    """
    prophet_df = stock_df[["date", "closing_price"]].rename(
        columns={"date": "ds", "closing_price": "y"}
    )

    prophet_df["ds"] = prophet_df["ds"].dt.tz_localize(None)

    start_date = prophet_df["ds"].max() + pd.Timedelta(days=1)
    cutoff_date = prophet_df["ds"].max() - pd.DateOffset(years=2)  # training on 2 years

    model = Prophet(
        changepoint_prior_scale=0.05,
        holidays_prior_scale=15,
        seasonality_prior_scale=10,
        weekly_seasonality=False,
        yearly_seasonality=True,
        daily_seasonality=False,
    )
    model.add_country_holidays(country_name="US")

    train = prophet_df[prophet_df["ds"] > cutoff_date]
    model.fit(train)

    future = model.make_future_dataframe(periods=120)  # forecast for 4 months
    forecast = model.predict(future).round({"yhat": 2})
    future_forecast = forecast[forecast["ds"] >= pd.to_datetime(start_date)][
        ["ds", "yhat"]
    ]  # only forecasted values

    return future_forecast, start_date
