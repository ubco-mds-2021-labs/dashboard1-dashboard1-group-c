from dash import html, dcc
import dash_bootstrap_components as dbc
import geopandas as gpd
import pandas as pd
import altair as alt
alt.data_transformers.enable('data_server')
alt.data_transformers.disable_max_rows()


# get the map shapefile from statcan
canada_df = gpd.read_file("https://www12.statcan.gc.ca/census-recensement/2011/geo/bound-limit/files-fichiers/gpr_000a11a_e.zip")

# Data Wrangling 
wind = pd.read_excel('../data/WindTurbineDatabase.xlsx', index_col = 0)
wind[['earlier_date', 'later_date']] = wind['Commissioning date'].str.split('/', 1, expand = True)
wind.earlier_date.fillna(wind['Commissioning date'], inplace=True)
wind = wind.drop(['Commissioning date', 'later_date'], axis = 1)
wind = wind.rename(columns = {'earlier_date' : 'Commissioning date'})
wind['Commissioning date'] = pd.to_numeric(wind['Commissioning date'])

# function for altair plot
def plot_province(prov,year):
    province = canada_df[canada_df["PRENAME"]==prov]
    
    base = alt.Chart(province).mark_geoshape(
    stroke='gray', 
    fill=None
    )
    
    wind_province = wind[wind["Province/Territory"]==prov]
    wind_province = wind[(wind["Province/Territory"]==prov) & (wind["Commissioning date"]<=year)]
    pts = alt.Chart(wind_province).mark_circle(color='red', opacity=0.3).encode(
    latitude='Latitude',
    longitude='Longitude'
    )


    alt_chart = base + pts
    return alt_chart.to_html()

CONTENT_STYLE = {
    "margin-left": "10rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
    'width': '100%', 
    'height': '400px',
}    

# layout component 
map = html.Iframe(id='altair_map',srcDoc=plot_province(prov = "British Columbia", year=1990),
style=CONTENT_STYLE)
