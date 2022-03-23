from dash import Dash
import dash_bootstrap_components as dbc
from flask_caching import Cache
import flask

server = flask.Flask(__name__)
app = Dash(
    name=__name__, 
    server=server,
    external_stylesheets=[dbc.themes.BOOTSTRAP]
)

cache = Cache(app.server, config={"CACHE_TYPE": "SimpleCache"})
