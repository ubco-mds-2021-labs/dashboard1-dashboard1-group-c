from dash import html
import altair as alt
from data import load_geo_data, load_data
from app import cache

alt.data_transformers.disable_max_rows()


# get the map and wind data
canada_df = load_geo_data()
wind = load_data(index=True)

# function for altair plot
@cache.memoize(timeout=50)
def plot_province(prov: str, year: int) -> str:
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
        region = canada_df[canada_df["name"] == prov]
    
    # geographic plot
    base = alt.Chart(
        region,
        title='Geographic location of the wind turbine'
    ).mark_geoshape(stroke="white").encode(color=alt.Color('name',legend=None))
    
    if prov is None:
        wind_province = wind[wind["Commissioning date"] <= year]
    else:
        wind_province = wind[wind["Province/Territory"] == prov]
        wind_province = wind[(wind["Province/Territory"] == prov) & (wind["Commissioning date"] <= year)]
    
    # location plot
    pts = alt.Chart(wind_province).mark_circle(
        color='red', 
        opacity=0.3,
        size = 5
    ).encode(
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
