from dash import html, dcc
import dash_bootstrap_components as dbc


SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "16rem",
    "padding": "2rem 1rem",
    "background-color": "#f8f9fa",
}

sidebar_header = dbc.Row(
    dbc.Col(html.H3("Controls"))
)

sidebar = html.Div(
    [
        sidebar_header,
        html.Hr(),
        dbc.Nav(
            [
                html.H5("Province"),
                dcc.Dropdown(
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
                ),
                html.H5("Year"),
                # dcc.Dropdown(
                #     [str(x) for x in range(1990, 2021)],
                #     id="year-selector"
                # ),
                dcc.Slider(1990,2021, 1, value=1990, marks=None,
                           tooltip={"placement": "bottom", "always_visible": True},id="year-selector")
            ],
            vertical=True
        )
    ],
    style=SIDEBAR_STYLE
)