from dash import Dash, html
import dash_bootstrap_components as dbc
from flask_caching import Cache
import flask
from dash.dependencies import Input, Output
from layout.layout import layout

from layout.models.models import pie_chart


server = flask.Flask(__name__)
app = Dash(
    name=__name__, 
    server=server,
    external_stylesheets=[dbc.themes.BOOTSTRAP]
)
app.layout = layout

cache = Cache(app.server, config={
    "CACHE_TYPE": "filesystem",
    "CACHE_DIR": "cache-directory"
})


#Callback for Model by Province Pie Chart
@app.callback(
    Output('model', 'srcDoc'),
    Input('province-selector', 'value'))

def update_output(selector):
        return pie_chart(selector)

if __name__ == "__main__":    
    app.run_server(debug=True, host="localhost")