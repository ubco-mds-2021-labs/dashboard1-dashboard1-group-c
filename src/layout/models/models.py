import altair as alt

from data import load_data
from app import cache


wind = load_data(index=True)

@cache.memoize(timeout=50)
def bar_chart(selector: str = None) -> str:
    """
    Function returns a bar chart of model count in each province
    
    Args:
        Selector: province. Defaults to None.

    Returns:
        A altair plot in html format for Dash
    """
    if selector is not None:
        province_model = wind.groupby(["Province/Territory","Model"], as_index=False).count().iloc[:, 0:3]
        province_model = province_model.rename(columns={"Project name":"Total"})
        selected = province_model[province_model["Province/Territory"] == selector]
    else:
        province_model = wind.groupby(["Model"], as_index=False).count().iloc[0:5, 0:3]
        selected = province_model.rename(columns={"Project name":"Total"})
        selector = "Canada"
        
    base = alt.Chart(selected, title=f'Models for {selector}').encode(
        x = 'Model',
        y = 'Total'
    )
    chart = base.mark_bar()

    return chart.to_html()

