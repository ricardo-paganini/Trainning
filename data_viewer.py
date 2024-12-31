import streamlit as st
import pandas as pd
import altair as alt

data = pd.read_csv('data/dataset_test.csv')

chart = alt.Chart(data).mark_line().encode(
    x = 'Platform',
    y = 'NA_Sales'
)

st.altair_chart(chart,use_container_width=True)