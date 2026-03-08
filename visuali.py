# visualization.py
import streamlit as st
import plotly.express as px

def plot_statewise_choropleth(df, metric_col, title, color_scale='Blues'):
    india_geojson = "https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson"

    fig = px.choropleth(
        df,
        geojson=india_geojson,
        featureidkey='properties.ST_NM',
        locations='state',
        color=metric_col,
        color_continuous_scale=color_scale,
        labels={metric_col: metric_col.replace("_", " ").title()}
    )

    fig.update_geos(fitbounds="locations", visible=False)
    fig.update_layout(title_text=title, title_x=0.5)
    st.plotly_chart(fig, use_container_width=True)