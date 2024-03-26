# APP

# https://www.youtube.com/watch?v=taZYIqC7VMM&t=1518s

# INSTALLATION
# https://shiny.posit.co/py/docs/install.html
# conda create -n stock2 python=3.11
# pip install shiny
# shiny run

# DEPLOYMENT
# https://login.shinyapps.io/login
# pip install rsconnect-python
# pip freeze > requirements.txt
# conda env export --name shiny2 > environment.yml (optional)
# rsconnect add --account jaroslavkotrba --name jaroslavkotrba --token XXXXXXXXXXXXXXXXXXXXXXXXXX --secret XXXXXXXXXXXXXXXXXXXXXXXXXX
# rsconnect list (optional)
# rsconnect deploy shiny . --entrypoint app:app

from shiny import App
from ui import app_ui
from server import server

app = App(app_ui, server)
