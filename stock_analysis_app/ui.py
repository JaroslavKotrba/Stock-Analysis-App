from shiny import ui
import shinyswatch
from shinywidgets import output_widget
from faicons import icon_svg  # sign icon

from ui_source.get_sp500_tickers import get_sp500_tickers

TITLE = "STOCK Analysis"

# Header
page_dependencies = ui.tags.head(
    ui.tags.link(rel="stylesheet", type="text/css", href="style.css"),
    # ui.tags.link(rel="icon", type="image/png", href="www/eagle.png"),
)

# Tickers
tickers = get_sp500_tickers()

app_ui = ui.page_navbar(
    shinyswatch.theme.lumen(),  # #158cba
    ui.nav_panel(
        "- ANALYSIS -",
        ui.layout_sidebar(
            # Sidebar
            ui.sidebar(
                ui.h2("Select a stock"),
                ui.input_selectize(
                    "stock_symbol",
                    "Stock Symbol",
                    tickers,
                    selected="MSFT | Microsoft",
                    multiple=False,
                ),
                ui.hr(),
                ui.download_button(
                    "downloadStockInfo",
                    "Download stock_info.csv",
                    icon=icon_svg("download"),
                    class_="btn-primary",
                ),
                ui.download_button(
                    "downloadStockHistory",
                    "Download stock_history.csv",
                    icon=icon_svg("download"),
                    class_="btn-primary",
                ),
                ui.download_button(
                    "downloadStockFinancial",
                    "Download stock_financial.csv",
                    icon=icon_svg("download"),
                    class_="btn-primary",
                ),
                position="left",
                width=350,
            ),
            # Main
            ui.h2(ui.output_ui("stock_abr")),
            ui.div(
                output_widget(
                    "stock_chart",
                    width="auto",
                    height="auto",
                )
            ),
            ui.navset_card_pill(
                ui.nav_panel("Company", ui.output_ui("stock_info")),
                ui.nav_panel("CEO", ui.output_ui("stock_ceo")),
            ),
        ),
        # Footer
        ui.HTML(
            '<p>Author\'s projects: <a href="https://jaroslavkotrba.com" style="text-decoration:none;" target="_blank">https://jaroslavkotrba.com</a></p>'
        ),
    ),
    ui.nav_panel(
        "- FINANCIALS -",
        # Main
        ui.navset_card_pill(
            ui.nav_panel("Company Summary", ui.output_ui("stock_fin")),
            ui.nav_panel("Income Statement", ui.output_ui("income_stat")),
        ),
        # Footer
        ui.HTML(
            '<p>Author\'s projects: <a href="https://jaroslavkotrba.com" style="text-decoration:none;" target="_blank">https://jaroslavkotrba.com</a></p>'
        ),
    ),
    ui.nav_panel(
        "- ABOUT -",
        # Main
        ui.navset_card_pill(
            ui.nav_panel("Our Story", "TODO - Our Story"),
            ui.nav_panel("Data Used", "TODO - Data Used"),
        ),
        # Footer
        ui.HTML(
            '<p>Author\'s projects: <a href="https://jaroslavkotrba.com" style="text-decoration:none;" target="_blank">https://jaroslavkotrba.com</a></p>'
        ),
    ),
    title=ui.tags.div(
        ui.img(
            src="eagle.png",
            height="60px",
            style="margin:5px;-webkit-filter:drop-shadow(0px 0px 0px #222)",
        ),
        ui.h6(
            " " + TITLE,
            style="margin-top:25px; margin-right:140px; font-style:italic; font-weight:bold;",
        ),
        style="display:flex;",
    ),
    inverse=True,
    underline=False,
    window_title="STOCK Analysis-Finance",  # Browser
    header=page_dependencies,
)
