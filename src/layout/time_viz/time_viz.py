import altair as alt
import pandas as pd

from data import load_data


def line_chart(province: str = None) -> str:
    data = load_data()
    if province:
        data = data.loc[data["Province/Territory"] == province]
    
    start_year = max(data["Commissioning date"].min() - 1, 1993)
    end_year = data["Commissioning date"].max()

    year_counts = data.groupby('Commissioning date').count()["OBJECTID"]
    count_dict = year_counts.to_dict()

    prev = count_dict.get(start_year, 0)
    count_dict[start_year] = prev
    for year in range(start_year + 1, end_year + 1):
        current = count_dict.get(year, 0) + prev
        count_dict[year] = current
        prev = current
    temp_list = list(count_dict.items())
    temp_list.sort(key=lambda x: x[0])
    cum_counts = pd.DataFrame(temp_list, columns=["Year", "Turbine Count"])

    chart: alt.Chart
    title: str
    if province:
        title = f"Cumulative Turbine Count in {province} Over Time"
    else:
        title = "Cumulative Turbine Count in Canada Over Time"
    chart = alt.Chart(cum_counts, title=title).mark_line(size=3).encode(
        x="Year:O",
        y="Turbine Count",
        tooltip="Turbine Count"
    ).properties(
        width=450
    )
    
    return chart.to_html()
