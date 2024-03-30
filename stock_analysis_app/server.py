from shiny import render
from shiny import ui
from shinywidgets import render_widget

from server_source.my_card import my_card
from server_source.load_stock_data import load_stock_data
from server_source.get_highest_paid_officer import get_highest_paid_officer
from server_source.load_stock_history import load_stock_history
from server_source.plotly_chart import plotly_chart


def app_server(input, output, session):

    # Selected stock
    @output
    @render.ui
    def symbol():
        html_symbol = ui.HTML(
            f"Selected stock: <span style='color:#158cba;'>{input.stock_symbol()}</span>"
        )
        return html_symbol

    # Chart
    @output
    @render_widget
    def stock_chart():
        stock_history = load_stock_history(input.stock_symbol(), "5y")  # CHANGE
        fig = plotly_chart(stock_history, window_mavg_short=30, window_mavg_long=90)
        return fig

    # Company
    @output
    @render.ui
    def stock_info():
        stock_info = load_stock_data(input.stock_symbol())

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
        stock_info = load_stock_data(input.stock_symbol())
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
        stock_info = load_stock_data(input.stock_symbol())

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
                "{:0,.1%}".format(stock_info["currentRatio"]),
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
