from shiny import ui
import shinyswatch
from shinywidgets import output_widget

TITLE = "STOCK Analysis"

# Header
page_dependencies = ui.tags.head(
    ui.tags.link(rel="stylesheet", type="text/css", href="style.css")
)

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
                    ["AAPL", "GOOG", "MSFT"],
                    selected="MSFT",
                    multiple=False,
                ),
                position="left",
                width=350,
            ),
            # Main
            ui.h2(ui.output_ui("symbol")),
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
            ui.nav_panel("Income Statement", "TODO - Income Statement"),
        ),
        # Footer
        ui.HTML(
            '<p>Author\'s projects: <a href="https://jaroslavkotrba.com" style="text-decoration:none;" target="_blank">https://jaroslavkotrba.com</a></p>'
        ),
    ),
    ui.nav_panel(
        "- ABOUT -",
        ui.row(
            ui.column(
                3,
                ui.panel_main(
                    ui.panel_sidebar(
                        ui.h2("Select company"),
                        ui.input_slider("m", "N", 0, 100, 20),
                    ),
                ),
            ),
            ui.column(
                9,
                ui.panel_main(
                    ui.navset_card_pill(
                        ui.nav_panel("Company Summary", "TODO - Summary"),
                        ui.nav_panel("Income Statement", "TODO - Income Statement"),
                    ),
                ),
            ),
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
