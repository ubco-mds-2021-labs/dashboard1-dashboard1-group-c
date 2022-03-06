from dash import html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
from .sidebar.sidebar import sidebar
from .models.models import plot_model


CONTENT_STYLE = {
    "margin-left": "10rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
}

content = html.Div(
    [html.H1("Count Models by Province"),plot_model], 
    id="dashboard-main",
    style=CONTENT_STYLE
)
layout = dbc.Container([sidebar, content])