from dash import html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
from .sidebar.sidebar import sidebar
from .total_capacity.totalCapacity import plot_totalCapacity

CONTENT_STYLE = {
    "margin-left": "20rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
}



content = html.Div(
    [html.H1("Wind Turbines in Canada"),plot_totalCapacity], 
    id="dashboard-main",
    style=CONTENT_STYLE
)
layout = dbc.Container([sidebar, content,])
