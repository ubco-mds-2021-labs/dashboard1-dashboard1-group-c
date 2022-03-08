from dash import html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
from .sidebar.sidebar import sidebar
from .total_capacity.total_capacity import plot_totalCapacity
from .time_viz.time_viz import line_chart


CONTENT_STYLE = {
    "margin-left": "10rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
}

I_FRAME_STYLE = {
    "width": "64%",
    "height": "400px"
}

content = html.Div(
    [
        html.H1("Wind Turbines in Canada"),
        html.Iframe(srcDoc=line_chart(), style=I_FRAME_STYLE, id="time-plot"),
        plot_totalCapacity,
        html.Hr()
    ], 
    id="dashboard-main",
    style=CONTENT_STYLE
)
layout = dbc.Container([sidebar, content,])
