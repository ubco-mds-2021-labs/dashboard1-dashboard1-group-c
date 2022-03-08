from dash import html, dcc
import dash_bootstrap_components as dbc


province = dcc.Dropdown(
    {
        "Alberta": "Alberta",
        "British Columbia": "British Columbia",
        "Manitoba": "Manitoba",
        "New Brunswick": "New Brunswick",
        "Newfoundland and Labrador": "Newfoundland",
        "Northwest Territories": "Northwest Territories",
        "Nova Scotia": "Nova Scotia",
        "Ontario": "Ontario",
        "Prince Edward Island": "Prince Edward Island",
        "Quebec": "Quebec",
        "Saskatchewan": "Saskatchewan",
                        "Yukon": "Yukon"
    },
    value=None,
    id="province-selector"
)

year = dcc.Slider(
    1990, 
    2021, 
    1, 
    value=1990, 
    marks=None,
    tooltip={"placement": "bottom", "always_visible": True}, 
    id="year-selector"
)

description = dbc.Col(
    class_name="bar", 
    style={'backgroundColor': 'grey', 'color': 'black'},
    children=[
        dbc.Row(
            "WIND TURBINES", 
            class_name="title",
            style={
                "font-size": "40px", 
                "padding-left": "20px", 
                "padding-right": "30px"
            }
        ),
        html.Br(),
        html.Br(),
        dbc.Row(
            dbc.Col(
                "This is a data visualization app that allows members of Natural Resources Canada planning committees to visually explore a dataset outlining existing windpower capacity in Canada.",
                style={
                    "font_family": "cursive", 
                    "font-size": "15px", 
                    "padding-left": "20px", 
                    "padding-right": "20px"
                }
            ),
        ),
        html.Br(),
        html.Br(),
        html.Br(),
        dbc.Label(
            "CONTROLS: ", 
            class_name="sub_title",
            style={
                "font-size": "30px", 
                "padding-left": "20px", 
                "padding-right": "20px"
            }
        ),
        html.Br(),
        dbc.Row(
            dbc.Col(
                "Select the province to get the information about wind turbines in that province. ",
                style={
                    "font_family": "cursive", 
                    "font-size": "15px", 
                    "padding-left": "20px", 
                    "padding-right": "20px"
                }
            ),
        ),
        dbc.Row(
            dbc.Col(
                "Also, slider lets you select the desired year so that cumulative count and geographic location of turbine can be seen for that year. ",
                style={
                    "font_family": "cursive", 
                    "font-size": "15px", 
                    "padding-left": "20px", 
                    "padding-right": "20px"
                }
            ),
        ),
        html.Br(),
        html.Br(),
        html.Br(),
    ]
)

#Sidebar
sidebar = dbc.Col(
    class_name="bar", 
    style={'backgroundColor': 'grey', 'color': 'black'},
    children=[
        dbc.Label(
            "Select Province: ", 
            class_name="sub_title",
            style={
                "font-size": "15px", 
                "padding-left": "20px", 
                "padding-right": "20px"
            }
        ),
        html.Br(),
        dbc.Row(
            province, 
            style={
                "font-size": "15px", 
                "padding-left": "20px",
                "padding-right": "20px", 
                "padding-top": "10px"
            }
        ),
        html.Br(),
        dbc.Label(
            "Slide to select Year: ", 
            class_name="sub_title",
            style={
                "font-size": "15px", 
                "padding-left": "20px", 
                "padding-right": "20px"
            }
        ),
        dbc.Row(
            year, 
            style={
                "font-size": "15px", 
                "padding-left": "20px",
                "padding-right": "20px", 
                "padding-top": "20px"
            }
        ),
        html.Br(),
        html.Br(),
        html.Br(),
        html.Br(),
        html.Br(),
        html.Br(),
        html.Br(),
        html.Br(),
    ]
)
