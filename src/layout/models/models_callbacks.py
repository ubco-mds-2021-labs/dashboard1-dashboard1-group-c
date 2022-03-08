from dash import Input, Output

from app import app
from .models import pie_chart

@app.callback(
    Output('model', 'srcDoc'),
    Input('province-selector', 'value')
)
def update_models(selector):
    return pie_chart(selector)