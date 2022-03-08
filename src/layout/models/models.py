from dash import html
import altair as alt
import pandas as pd


wind = pd.read_excel('../data/WindTurbineDatabase.xlsx', index_col = 0)


def pie_chart(selector='Alberta'):  
    
    province_model = wind.groupby(["Province/Territory","Model"], as_index=False).count().iloc[:, 0:3]
    province_model = province_model.rename(columns={"Project name":"Total"})
    selected = province_model[province_model["Province/Territory"] == selector]
    base = alt.Chart(selected,title='Model by Province').encode(
    theta=alt.Theta("Total:Q", stack=True), color=alt.Color("Model:N")
    )
    pie = base.mark_arc(outerRadius=160,innerRadius=80)
    text = base.mark_text(radius=190, size=10).encode(text="Model:N")

    chart = pie + text
    return chart.to_html()

