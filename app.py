import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv('vehicles_us.csv')
# Header
st.header('Vehicle Advertisement Dashboard')

# Histogram
if st.checkbox('Show price distribution'):
    fig = px.histogram(
        df,
        x='price',
        title='Distribution of Vehicle Prices'
    )
    st.plotly_chart(fig)

# Scatter plot
if st.checkbox('Show price vs mileage'):
    fig = px.scatter(
        df,
        x='odometer',
        y='price',
        title='Price vs Mileage'
    )
    st.plotly_chart(fig)
