from dash import Dash, html
import dash_bootstrap_components as dbc
from flask_caching import Cache
import flask
from dash.dependencies import Input, Output
from layout.layout import layout
from layout.map.map import map, plot_province

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
    @app.callback(
        Output('altair_map','srcDoc'), # Specifies where the output of plot_cars() "goes"
        Input('province-selector', 'value'),
        Input('year-selector', 'value'))
    
    def update_map(prov,year):  
        return plot_province(prov,year)
    app.run_server(debug=True, host="localhost")
    
    