from shiny import render
from shiny import ui
import yfinance as yf
from server_source.my_card import my_card
from server_source.plotly_chart import plotly_chart


def app_server(input, output, session):

    # Selected stock
    @output
    @render.text
    def symbol():
        return f"Selected stock: {input.stock_symbol()}"

    # Build a company summary
    @output
    @render.ui
    def stock_info_ui():

        symbol = input.stock_symbol()
        stock = yf.Ticker(symbol)
        stock_info = stock.info

        app_ui = ui.row(
            ui.h5("Company information"),
            my_card("Industry", stock_info["industry"], bg_color="bg-dark"),
            my_card(
                "Fulltime Employees",
                "{:0,.0f}".format(stock_info["fullTimeEmployees"]),
                bg_color="bg-primary",
            ),
            my_card(
                "Website",
                ui.a(
                    stock_info["website"],
                    style="text-decoration:none; font-weight:bold;",
                    href=stock_info["website"],
                    target_="blank",
                ),
                bg_color="bg-dark",
            ),
            ui.hr(),
            ui.h5("Finantial ratios"),
            my_card(
                "Profit Margin",
                "{:0,.1%}".format(stock_info["profitMargins"]),
                bg_color="bg-dark",
            ),
        )
        return app_ui
