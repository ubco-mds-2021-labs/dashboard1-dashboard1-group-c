from data import load_data
import altair as alt
import pandas as pd


def line_chart(province: str = None) -> str:
    data = load_data()
    if province:
        data = data.loc[data["Province/Territory"] == province]
    
    start_year = max(data["Commissioning date"].min() - 1, 1993)
    end_year = data["Commissioning date"].max()

    year_counts = data.groupby('Commissioning date').count()["OBJECTID"]
    # cum_counts = [None for _ in range(year_counts.size)]
    # cum_counts[0] = year_counts.iloc[0]
    # for i in range(1, len(cum_counts)):
    #     cum_counts[i] = year_counts.iloc[i] + cum_counts[i - 1]

    # cum_counts = pd.Series(data=cum_counts, index=year_counts.index, name="Turbine Count", dtype=int)
    # cum_counts = pd.DataFrame(cum_counts).reset_index().rename(columns={"Commissioning date": "Year"})
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
        x="Year",
        y="Turbine Count",
        tooltip="Turbine Count"
    )
    
    return chart.to_html()


if __name__ == "__main__":
    print(load_data())