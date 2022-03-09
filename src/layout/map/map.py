from dash import html, dcc
import dash_bootstrap_components as dbc
import geopandas as gpd
import altair as alt

from data import load_geo_data

alt.data_transformers.disable_max_rows()


# get the map shapefile from statcan
canada_df = gpd.read_file("https://www12.statcan.gc.ca/census-recensement/2011/geo/bound-limit/files-fichiers/gpr_000a11a_e.zip")
wind = load_geo_data()

# function for altair plot
def plot_province(prov,year):
    if prov is None:
        url_geojson = 'https://raw.githubusercontent.com/johan/world.geo.json/master/countries/CAN.geo.json'
        region = alt.Data(url=url_geojson, format=alt.DataFormat(property='features',type='json'))
    else:
        region = canada_df[canada_df["PRENAME"]==prov]
    
    base = alt.Chart(region).mark_geoshape(
        stroke='gray', 
        fill=None
    ).project('albers')
    
    if prov is None:
        wind_province = wind[wind["Commissioning date"] <= year]
    else:
        wind_province = wind[wind["Province/Territory"] == prov]
        wind_province = wind[(wind["Province/Territory"] == prov) & (wind["Commissioning date"] <= year)]
    pts = alt.Chart(wind_province).mark_circle(color='red', opacity=0.3).encode(
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
