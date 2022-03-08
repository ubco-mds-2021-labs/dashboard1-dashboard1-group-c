from dash import Input, Output

from app import app
from .time_viz import line_chart

@app.callback(
    Output("time-plot", "srcDoc"),
    Input("province-selector", "value")
)
def update_cumulative_count(province: str) -> str:
    return line_chart(province)