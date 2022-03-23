from dash import Input, Output

from app import app
from .models import bar_chart

@app.callback(
    Output('model', 'srcDoc'),
    Input('province-selector', 'value')
)
def update_models(selector):
    return bar_chart(selector)