from dash import html
import dash_bootstrap_components as dbc

from .sidebar.sidebar import sidebar
from .map.map import map
from .models.models import pie_chart
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
        map,
        plot_totalCapacity,
        html.Iframe(srcDoc=pie_chart(), id='model',style={'border-width': '0', 'width': '100%', 'height': '400px'}),
        html.Hr()
    ], 
    id="dashboard-main",
    style=CONTENT_STYLE
)

layout = dbc.Container([sidebar, content])
