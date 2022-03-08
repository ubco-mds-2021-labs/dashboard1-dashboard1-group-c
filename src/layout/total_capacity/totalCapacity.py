#Imports
from dash import html
import altair as alt
import pandas as pd

#Reading data
wind = pd.read_excel('../data/WindTurbineDatabase.xlsx', index_col = 0)

#Function for creating bar graph for total capacity as per province
def plot_altair(ycol='Alberta'):  
    
    province_capacity = wind.groupby("Province/Territory", as_index=False).aggregate("sum").sort_values(by="Turbine rated capacity (kW)", ascending=False)
    province_capacity["Turbine rated capacity (kW)"] /= 1000
    province_capacity = province_capacity.rename(columns={"Turbine rated capacity (kW)": "Total Capacity (MW)","Province/Territory":"Province"})

    chart=alt.Chart(province_capacity, title="Total Wind Capacity by Province").mark_bar().encode(
        x=alt.X("Total Capacity (MW)"),
        y=alt.Y("Province", sort=province_capacity["Province"].to_list()),
        color=alt.condition(
            alt.datum.Province == ycol,  
            alt.value('red'),     
            alt.value('lightgrey')),
         tooltip=["Province","Total Capacity (MW)","Total project capacity (MW)"]
    )
    return chart.to_html()

#Plot to save the output of the total capacity bar graph
plot_totalCapacity=html.Iframe(id='bar',
                                    style={'border-width': '0', 
                                            'width': '100%', 
                                            'height': '400px', 
                                            "margin-left": "20rem",
                                            "margin-right": "2rem",
                                            "padding": "2rem 1rem",},
                                    srcDoc=plot_altair(ycol='Alberta'))