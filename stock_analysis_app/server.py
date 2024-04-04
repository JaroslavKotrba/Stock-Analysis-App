from shiny import render, ui, reactive
from shinywidgets import render_widget
import pandas as pd
import yfinance as yf

from server_source.my_card import my_card
from server_source.plotly_chart import plotly_chart
from server_source.get_highest_paid_officer import get_highest_paid_officer
from server_source.load_income_statement import load_income_statement


def app_server(input, output, session):

    # Reactive Stock
    @reactive.Calc
    def stock():
        symbol = str(input.stock_symbol()).split(" | ")[0].strip()
        return yf.Ticker(symbol)

    # Selected Stock
    @output
    @render.ui
    def stock_abr():
        if input.stock_symbol():
            stock_symbol = str(input.stock_symbol()).split(" | ")[1]
            html_content = f"The selected stock: <span style='color:#158cba;'>{stock_symbol}</span>"
        else:
            html_content = (
                "<span style='color:red;'>STOCK has not been selected!</span>"
            )
        return ui.HTML(html_content)

    # Save Stock Info
    @render.download(filename="stock_info.csv")
    def downloadStockInfo():
        stock_info = stock().info
        df = pd.DataFrame(list(stock_info.items()), columns=["Feature", "Value"])
        df = df[df["Feature"] != "companyOfficers"]
        yield df.to_csv(index=False, sep=",")

    # Save Stock History
    @render.download(filename="stock_history.csv")
    def downloadStockHistory():
        period = "5y"  # CHANGE
        stock_history = stock().history(period=period)
        yield stock_history.to_csv(index=True, sep=",")

    # Save Stock Financial
    @render.download(filename="stock_financial.csv")
    def downloadStockFinancial():
        stock_incomestmt = load_income_statement(stock())
        yield stock_incomestmt.to_csv(index=False, sep=",")

    # Chart
    @output
    @render_widget
    def stock_chart():
        period = "50y"  # CHANGE
        window_mavg_short = 30
        window_mavg_long = 90

        stock_history = stock().history(period=period)
        fig = plotly_chart(
            stock_history,
            window_mavg_short=window_mavg_short,
            window_mavg_long=window_mavg_long,
        )
        return fig

    # Company
    @output
    @render.ui
    def stock_info():
        stock_info = stock().info

        box_ui = ui.row(
            ui.h5("Company Information"),
            my_card(
                "Industry",
                stock_info["industry"],
                bg_color="bg-dark",
            ),
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
        )
        return box_ui

    # CEO
    @output
    @render.ui
    def stock_ceo():
        stock_info = stock().info
        title, name, totalPay = get_highest_paid_officer(stock_info["companyOfficers"])

        box_ui = ui.row(
            ui.h5("Finantial Ratios"),
            my_card(
                "Title",
                title,
                bg_color="bg-dark",
            ),
            my_card(
                "Name",
                name,
                bg_color="bg-primary",
            ),
            my_card(
                "Total Pay",
                "${:0,.0f}".format(totalPay),
                bg_color="bg-dark",
            ),
        )
        return box_ui

    # Company Summary
    @output
    @render.ui
    def stock_fin():
        stock_info = stock().info

        box_ui = ui.row(
            ui.h5("Finantial Ratios"),
            my_card(
                "Revenue Growth",
                "{:0,.1%}".format(stock_info["revenueGrowth"]),
                bg_color="bg-dark",
            ),
            my_card(
                "Profit Margin",
                "{:0,.1%}".format(stock_info["profitMargins"]),
                bg_color="bg-primary",
            ),
            my_card(
                "Current Ratio",
                "{:0,.2f}".format(stock_info["currentRatio"]),
                bg_color="bg-dark",
            ),
            ui.div(style="height:18px;"),
            ui.hr(),
            ui.h5("Finantial Operations"),
            my_card(
                "Total Revenue",
                "${:0,.0f}".format(stock_info["totalRevenue"]),
                bg_color="bg-dark",
            ),
            my_card(
                "Net Income",
                "${:0,.0f}".format(stock_info["netIncomeToCommon"]),
                bg_color="bg-primary",
            ),
            my_card(
                "Operating Cash Flow",
                "${:0,.0f}".format(stock_info["operatingCashflow"]),
                bg_color="bg-dark",
            ),
            my_card(
                "EBITDA",
                "${:0,.0f}".format(stock_info["ebitda"]),
                bg_color="bg-dark",
            ),
            my_card(
                "Market Capitalisation",
                "${:0,.0f}".format(stock_info["marketCap"]),
                bg_color="bg-primary",
            ),
            my_card(
                "Enterprise Value",
                "${:0,.0f}".format(stock_info["enterpriseValue"]),
                bg_color="bg-dark",
            ),
        )
        return box_ui

    # Income Statement
    @output
    @render.table
    def income_stat():
        stock_incomestmt = load_income_statement(stock())
        return stock_incomestmt
