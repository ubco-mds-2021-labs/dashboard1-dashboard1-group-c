from dash import Input, Output

from app import app
from .map import plot_province

@app.callback(
    Output('altair_map','srcDoc'), # Specifies where the output of plot_cars() "goes"
    Input('province-selector', 'value'),
    Input('year-selector', 'value'))

def update_map(prov,year):  
    return plot_province(prov,year)