from shiny import ui
import shinyswatch

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
                ui.h2("Select company"), ui.input_slider("n", "N", 0, 100, 20), width=3
            ),
            ui.panel_main(
                ui.h2(ui.output_text("txt")),
                ui.navset_card_pill(
                    ui.nav_panel("Company Summary", "TODO - Summary"),
                    ui.nav_panel("Income Statement", "TODO - Income Statement"),
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
