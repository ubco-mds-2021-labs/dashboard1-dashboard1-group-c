from dash import html, dcc
import dash_bootstrap_components as dbc
import geopandas as gpd
import altair as alt
import pathlib
from data import load_geo_data

alt.data_transformers.disable_max_rows()


# get the map and wind data
canada_df =  gpd.read_file("../data/canada.geojson")
wind = load_geo_data()

# function for altair plot
def plot_province(prov,year):
    """
    A function that plot the location of wind turbine on a geographic map.
    
    Parameters:
    -----------
    prov: the 12 Canadian provinces/territories.
    year: range from (1990 - 2021)
    
    Returns:
    --------
    A altair plot in html format for Dash
    """
    
    if prov is None:
        region = canada_df
    else:
        region = canada_df[canada_df["name"]==prov]
    
    # geographic plot
    base = alt.Chart(region,title='Geographic location of the wind turbine').mark_geoshape(stroke="white").encode(color=alt.Color('name',legend=None))
    
    if prov is None:
        wind_province = wind[wind["Commissioning date"] <= year]
    else:
        wind_province = wind[wind["Province/Territory"] == prov]
        wind_province = wind[(wind["Province/Territory"] == prov) & (wind["Commissioning date"] <= year)]
    
    # location plot
    pts = alt.Chart(wind_province).mark_circle(color='black', opacity=0.3,size = 5).encode(
    latitude='Latitude',
    longitude='Longitude'
    )

    alt_chart = base + pts
    return alt_chart.to_html()

CONTENT_STYLE = {
    'border-width': '0', 
    'width': '200%', 
    'height': '400px',
    'align-items': 'end'
}    

# layout component 
map = html.Iframe(
    id='altair_map',
    srcDoc=plot_province(prov = "British Columbia", year=1990),
    style=CONTENT_STYLE
)
