import altair as alt

from data import load_raw_data


wind = load_raw_data()

def pie_chart(selector='Alberta'):  
    province_model = wind.groupby(["Province/Territory","Model"], as_index=False).count().iloc[:, 0:3]
    province_model = province_model.rename(columns={"Project name":"Total"})
    if selector is not None:
        selected = province_model[province_model["Province/Territory"] == selector]
    else:
        selected = province_model
        selector = "Canada"
    base = alt.Chart(selected, title=f'Models for {selector}').encode(
        theta=alt.Theta("Total:Q", stack=True), 
        color=alt.Color("Model:N")
    )
    pie = base.mark_arc(outerRadius=160,innerRadius=80)
    text = base.mark_text(radius=190, size=10).encode(text="Model:N")

    chart = pie + text
    return chart.to_html()

