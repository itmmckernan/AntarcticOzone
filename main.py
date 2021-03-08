import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

points = pd.read_csv(open("points.csv", "r"))
pd.options.plotting.backend = "plotly"
print(points)
figure = go.Figure()
figure.add_trace(go.Scattergeo(lon=points['Lon'], lat=points['Lat150'], fill='toself', name='150 DU', line=dict(color='#ff7f0e')))
figure.add_trace(go.Scattergeo(lon=points['Lon'], lat=points['Lat200'], fill='toself', name='200 DU', line=dict(color='#2ca02c')))

figure.update_layout(
    title_text='Ozone Levels in the Antarctic',
    showlegend=True,
    geo=dict(
        showland=True,
        showcountries=True,
        showocean=True,
        countrywidth=0.75,
        landcolor='rgb(255, 255, 255)',
        lakecolor='rgb(255, 255, 255)',
        oceancolor='rgb(200, 200, 255)',
        projection=dict(
            type='orthographic',
            rotation=dict(
                lon=0,
                lat=-90,
                roll=0
            )
        ),
        lonaxis=dict(
            showgrid=True,
            gridcolor='rgb(102, 102, 102)',
            gridwidth=0.5
        ),
        lataxis=dict(
            showgrid=True,
            gridcolor='rgb(102, 102, 102)',
            gridwidth=0.5
        )
    )
)

figure.show()
with open("output.html", "w+") as file:
    file.write(figure.to_html())
