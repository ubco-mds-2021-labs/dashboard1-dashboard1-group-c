from dash import html
import dash_bootstrap_components as dbc

from .sidebar.sidebar import sidebar


CONTENT_STYLE = {
    "margin-left": "10rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
}

content = html.Div(
    [html.H1("Title...")], 
    id="dashboard-main",
    style=CONTENT_STYLE
)
layout = dbc.Container([sidebar, content])