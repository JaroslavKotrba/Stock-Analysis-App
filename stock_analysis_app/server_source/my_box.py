from shiny import ui


def my_box(title, value):
    """
    Function to generate a box for text
    """
    box_ui = ui.div(
        ui.h5(title),
        ui.div(value, style="margin:5px;"),
    )

    return box_ui
