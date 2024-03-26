from shiny import ui

app_ui = ui.page_fluid(
    ui.h2("Hello Shiny"),
    ui.input_slider("n", "N", 0, 100, 20),
    ui.output_text_verbatim("txt"),
)
