from shiny import ui
import shinyswatch
from shinywidgets import output_widget
from faicons import icon_svg  # sign icon

from ui_source.get_sp500_tickers import get_sp500_tickers

TITLE = "Stock Analysis"

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
                ui.div(style="height:7px;"),
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
                    "Download stock_fin.csv",
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
            ui.input_selectize(
                "months_to_predict",
                "Select how many months in future",
                [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12],
                selected=4,
                multiple=False,
                # width="150px",
            ),
            ui.navset_card_pill(
                ui.nav_panel("Company", ui.output_ui("stock_info")),
                ui.nav_panel("CEO", ui.output_ui("stock_ceo")),
            ),
        ),
        # Footer
        ui.HTML(
            f"""
            <div style="text-align:center;">
                <p>Author's projects: <a href="https://jaroslavkotrba.com" style="text-decoration:none;" target="_blank">https://jaroslavkotrba.com</a></p>
                <a href="https://www.linkedin.com/in/jaroslav-kotrba/" target="_blank" style="font-size:24px;">{icon_svg("linkedin")}</a>
                <a href="https://github.com/JaroslavKotrba" target="_blank" style="font-size:24px;">{icon_svg("github")}</a>
                <a href="https://www.facebook.com/jaroslav.kotrba.9/" target="_blank" style="font-size:24px;">{icon_svg("facebook")}</a>
                <p>Copyright &copy; 2024</p>
            </div>
            """
        ),
    ),
    ui.nav_panel(
        "- FINANCIAL -",
        # Main
        ui.navset_card_pill(
            ui.nav_panel("Company Summary", ui.output_ui("stock_fin")),
            ui.nav_panel("Income Statement", ui.output_ui("income_stat")),
        ),
        # Footer
        ui.HTML(
            f"""
            <div style="text-align:center;">
                <p>Author's projects: <a href="https://jaroslavkotrba.com" style="text-decoration:none;" target="_blank">https://jaroslavkotrba.com</a></p>
                <a href="https://www.linkedin.com/in/jaroslav-kotrba/" target="_blank" style="font-size:24px;">{icon_svg("linkedin")}</a>
                <a href="https://github.com/JaroslavKotrba" target="_blank" style="font-size:24px;">{icon_svg("github")}</a>
                <a href="https://www.facebook.com/jaroslav.kotrba.9/" target="_blank" style="font-size:24px;">{icon_svg("facebook")}</a>
                <p>Copyright &copy; 2024</p>
            </div>
            """
        ),
    ),
    ui.nav_panel(
        "- ABOUT -",
        # Main
        ui.navset_card_pill(
            ui.nav_panel("About Company", ui.output_ui("stock_about")),
            ui.nav_panel("Data Used", ui.output_ui("stock_api")),
        ),
        # Footer
        ui.HTML(
            f"""
            <div style="text-align:center;">
                <p>Author's projects: <a href="https://jaroslavkotrba.com" style="text-decoration:none;" target="_blank">https://jaroslavkotrba.com</a></p>
                <a href="https://www.linkedin.com/in/jaroslav-kotrba/" target="_blank" style="font-size:24px;">{icon_svg("linkedin")}</a>
                <a href="https://github.com/JaroslavKotrba" target="_blank" style="font-size:24px;">{icon_svg("github")}</a>
                <a href="https://www.facebook.com/jaroslav.kotrba.9/" target="_blank" style="font-size:24px;">{icon_svg("facebook")}</a>
                <p>Copyright &copy; 2024</p>
            </div>
            """
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
            style="margin-top:26.5px; margin-right:50px; font-family:'Baskerville', serif; font-weight: 900; font-style:italic; color:#158cba;",  # text-shadow: -1px -1px 0 #158cba, 1px -1px 0 #158cba, -1px 1px 0 #158cba, 1px 1px 0 #158cba;
        ),
        style="display:flex;",
    ),
    inverse=True,
    underline=False,
    window_title="STOCK Analysis-Finance",  # Browser
    header=page_dependencies,
)
