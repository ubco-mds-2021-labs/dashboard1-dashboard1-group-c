from dash import Input, Output

from app import app
from .total_capacity import plot_capacity

@app.callback(
    Output('capacity-plot', 'srcDoc'),
    Input('province-selector', 'value'))
def update_capacity(ycol):
    return plot_capacity(ycol)