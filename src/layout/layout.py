from dash import html
import dash_bootstrap_components as dbc

from .sidebar.sidebar import sidebar, description
from .map.map import map
from .models.models import pie_chart
from .total_capacity.total_capacity import plot_totalCapacity
from .time_viz.time_viz import line_chart


row1 = html.Div(
    [
        dbc.Row(
            [
                dbc.Col(description, width=3),
                dbc.Col(plot_totalCapacity, width=5),
                dbc.Col(
                    html.Iframe(
                        srcDoc=pie_chart(), 
                        id='model', 
                        style={
                            'border-width': '0', 
                            'width': '200%', 
                            'height': '400px'
                        }
                    ), 
                    width=4
                )
            ]
        ),
    ],
    className='row',
    style={'height': '30%', 'background-color': 'white', "padding-left": "20px"}
)

row2 = html.Div(
    [
        dbc.Row(
            [
                dbc.Col(sidebar, width=3),
                dbc.Col(map, width=4),
                dbc.Col(
                    html.Iframe(
                        srcDoc=line_chart(), 
                        style={
                            'border-width': '0', 
                            'width': '160%', 
                            'height': '400px', 
                            'align-items': 'end'
                        }, 
                        id="time-plot"
                    ), 
                    width=3
                )
            ]
        ),
    ],
    className='row',
    style={'height': '30%', 'background-color': 'white', "padding-left": "20px"}
)

layout = html.Div(
    [
        html.Br(),
        html.Br(),
        html.Br(),
        dbc.Row(row1),
        dbc.Row(row2),
    ]
)
