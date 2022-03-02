from dash import Dash, html
import dash_bootstrap_components as dbc
from flask_caching import Cache
import flask


server = flask.Flask(__name__)
app = Dash(
    name=__name__, 
    server=server,
    external_stylesheets=[dbc.themes.BOOTSTRAP]
)

cache = Cache(app.server, config={
    "CACHE_TYPE": "filesystem",
    "CACHE_DIR": "cache-directory"
})

if __name__ == "__main__":
    layout = dbc.Container(
        [
            html.H1("Insert Title Here...")
        ]
    )
    app.layout = layout
    app.run_server(debug=True, host="localhost")