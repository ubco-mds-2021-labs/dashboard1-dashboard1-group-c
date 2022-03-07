from dash import html
import dash_bootstrap_components as dbc
from .sidebar.sidebar import sidebar
from .models.models import pie_chart


CONTENT_STYLE = {
    "margin-left": "10rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
}

#I_FRAME_STYLE = {
   # "width": "100%",
   # "height": "600px"
#}
content = html.Div([
    html.H1("Title..."),
    html.Iframe(srcDoc=pie_chart(), id='model',style={'border-width': '0', 'width': '100%', 'height': '400px'})
    ],
    id="dashboard-main",
    style=CONTENT_STYLE
)
layout = dbc.Container([sidebar, content])