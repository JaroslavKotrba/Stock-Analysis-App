# https://getbootstrap.com/docs/5.0/components/card/
from shiny import ui


def my_card(title, value, width=4, bg_color="bg-info", text_color="text-white"):
    """
    Function to generate a boostrap 5 card
    """
    card_ui = ui.div(
        ui.div(
            ui.div(
                ui.div(ui.h4(title, class_="mb-2"), class_="card-title"),
                ui.div(value, class_="card-text"),
                class_="card-body flex-fill",
            ),
            class_=f"card {text_color} {bg_color}",
            style="flex-grow:1; margin:5px;",
        ),
        class_=f"col-md-{width} d-flex",
    )

    return card_ui
