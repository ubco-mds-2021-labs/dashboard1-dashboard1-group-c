from dash import html
import dash_bootstrap_components as dbc

from .sidebar.sidebar import sidebar
from .time_viz.time_viz import line_chart


CONTENT_STYLE = {
    "margin-left": "10rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
}

I_FRAME_STYLE = {
    "width": "50%",
    "height": "400px"
}

content = html.Div(
    [
        html.H1("Title..."),
        html.Iframe(srcDoc=line_chart(), style=I_FRAME_STYLE, id="time-plot"),
        html.Hr()
    ], 
    id="dashboard-main",
    style=CONTENT_STYLE
)
layout = dbc.Container([sidebar, content])