from dash import html
import altair as alt
import pandas as pd


wind = pd.read_excel('../data/WindTurbineDatabase.xlsx', index_col = 0)


def plot_altair(choice='Alberta'):  
    
    province_model = wind.groupby(["Province/Territory","Model"], as_index=False).count().iloc[:, 1:3]
    province_model = province_model.rename(columns={"Project name":"Total"})
    selected = province_model[province_model["Province/Territory"] == choice]
    base = alt.Chart(selected,title='Model by Province').encode(
    theta=alt.Theta("Total:Q", stack=True), color=alt.Color("Model:N")
    )
    pie = base.mark_arc(outerRadius=160,innerRadius=80)
    text = base.mark_text(radius=190, size=10).encode(text="Model:N")

    chart = pie + text
    return chart.to_html()


plot_model=html.Iframe(id='model',
                                    style={'border-width': '0', 
                                            'width': '100%', 
                                            'height': '400px', 
                                            "margin-left": "20rem",
                                            "margin-right": "2rem",
                                            "padding": "2rem 1rem",},
                                    srcDoc=plot_altair(choice='Alberta'))