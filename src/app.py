from dash import Dash, html
import dash_bootstrap_components as dbc
from flask_caching import Cache
import flask
from dash.dependencies import Input, Output
from layout.layout import layout
from .sidebar.sidebar import sidebar
from .models.models import plot_model


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
    # layout = dbc.Container(
    #     [
    #         html.H1("Insert Title Here...")
    #     ]
    # )
    app.layout = layout
    
    #Callback for Model by Province Pie Chart
    @app.callback(
        Output('model', 'srcDoc'),
        Input('province-selector', 'value'))
    def update_output(choice):
        return plot_altair(choice)
    
    app.run_server(debug=True, host="localhost")