# APP

# https://www.youtube.com/watch?v=taZYIqC7VMM&t=1518s

# INSTALLATION
# https://shiny.posit.co/py/docs/install.html
# conda create -n stock2 python=3.11
# extension "Shiny for Python"
# pip install shiny
# shiny run

# DEPLOYMENT
# https://login.shinyapps.io/login
# pip install rsconnect-python
# pip freeze > requirements.txt
# conda env export --name stock2 > environment.yml (optional)
# rsconnect add --account jaroslavkotrba --name jaroslavkotrba --token XXXXXXXXXXXXXXXXXXXXXXXXXX --secret XXXXXXXXXXXXXXXXXXXXXXXXXX
# rsconnect list (optional)
# rsconnect deploy shiny . --entrypoint app:app

# TODO: links to social media
# TODO: download data

from shiny import App
from ui import app_ui
from server import app_server

from pathlib import Path

www_dir = Path(__file__).parent / "www"
app = App(app_ui, app_server, static_assets=www_dir)
