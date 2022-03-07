from dash import html, dcc
import dash_bootstrap_components as dbc

# Province selector
province=dcc.Dropdown(
                    
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
                    value="Alberta",
                    id="province-selector"
                )

# Year selector
year=dcc.Dropdown(
                    [str(x) for x in range(1990, 2021)],
                    id="year-selector"
                )

# Description
description = dbc.Col(class_name="bar",style={'backgroundColor':'grey','color':'black'},
                  children=[dbc.Row(
                      dbc.Col("This is a data visualization ",
                                    style={"font_family": "cursive","font-size":"20px","padding-left": "20px","padding-right": "20px",}),
                      ),
                      dbc.Row(
                      dbc.Col("app that allows members ",
                                    style={"font-size":"20px","padding-left": "20px","padding-right": "20px",}),
                      ),
                      dbc.Row(
                      dbc.Col("of Natural Resources Canada ",
                                    style={"font-size":"20px","padding-left": "20px","padding-right": "20px",}),
                      ),
                      
                      dbc.Row(
                        dbc.Col(" planning committees to visually",
                                    style={"font-size":"20px","padding-left": "20px","padding-right": "20px"}),
                      ),
                      
                      dbc.Row(
                        dbc.Col(" explore a dataset outlining",
                                    style={"font-size":"20px","padding-left": "20px","padding-right": "20px"}),
                      ),
                      dbc.Row(
                        dbc.Col("windpower capacity in Canada.",
                                    style={"font-size":"20px","padding-left": "20px","padding-right": "20px"}),
                      ),
                      
                
                    html.Br(),
                    dbc.Row(
                        dbc.Col("Choose the control above",
                                    style={"font-size":"20px","padding-left": "20px","padding-right": "20px"}),
                      ),
                    dbc.Row(
                        dbc.Col("to change your selection.",
                                    style={"font-size":"20px","padding-left": "20px","padding-right": "20px"}),
                      ),
                    html.Br(),
                    html.Br(),
                    html.Br(),
                    html.Br(),
                    html.Br(),
                    html.Br(),
                    html.Br(),
                    html.Br(),
],)

#Sidebar
sidebar = dbc.Col(class_name="bar",style={'backgroundColor':'grey','color':'black'},
                  children=[
                      dbc.Row("WIND TURBINES",class_name="title",
                                    style={"font-size":"40px","padding-left": "20px","padding-right": "30px","padding-top": "20px"}),
 
html.Br(),
html.Br(),
dbc.Label("CONTROLS: ",class_name="sub_title",
          style={"font-size":"30px","padding-left": "20px","padding-right": "20px","padding-top": "20px"}),
html.Br(),
html.Br(),
dbc.Row(province, style={"font-size":"15px","padding-left": "20px","padding-right": "20px","padding-top": "10px"}),
html.Br(),
dbc.Row(year, style={"font-size":"15px","padding-left": "20px","padding-right": "20px","padding-top": "20px"}),
html.Br(),
html.Br(),
],)




