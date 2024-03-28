from shiny import ui
import shinyswatch
from shinywidgets import output_widget

TITLE = "STOCK Analysis"

page_dependencies = ui.tags.head(
    ui.tags.link(rel="stylesheet", type="text/css", href="style.css")
)

app_ui = ui.page_navbar(
    shinyswatch.theme.lumen(),
    ui.nav_panel(
        "- ANALYSIS -",
        ui.layout_sidebar(
            ui.panel_sidebar(
                ui.h2("Select a stock"),
                ui.input_selectize(
                    "stock_symbol",
                    "Stock Symbol",
                    ["AAPL", "GOOG", "MSFT"],
                    selected="MSFT",
                    multiple=False,
                ),
                width=3,
            ),
            ui.panel_main(
                ui.h2(ui.output_text("symbol")),
                ui.div(
                    output_widget(
                        "stock_chart_widget",
                        width="auto",
                        height="auto",  # class_="card"
                    )
                ),
                ui.navset_card_pill(
                    ui.nav_panel("Company Summary", ui.output_ui("stock_info_ui")),
                    ui.nav_panel(
                        "Income Statement", ui.output_table("income_statement_table")
                    ),
                ),
            ),
        ),
    ),
    ui.nav_panel(
        "- STATEMENTS -",
        ui.panel_main(
            ui.navset_card_pill(
                ui.nav_panel("Company Summary", "TODO - Summary"),
                ui.nav_panel("Income Statement", "TODO - Income Statement"),
            ),
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
            style="margin-top:25px; margin-right:50px; font-style:italic; font-weight:bold;",
        ),
        style="display:flex;",
    ),
    # bg="white",
    inverse=True,
    underline=False,
    header=page_dependencies,
)
