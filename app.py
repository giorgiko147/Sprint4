import pandas as pd
import streamlit as st
import plotly.express as px

df = pd.read_csv('vehicles_us.csv')

st.header('Vehicle Advertisement Dashboard')

st.write(
    'This dashboard explores used vehicle advertisement data. '
    'Select which vehicles are included in the graphs below.'
)

# Creating the filter
#Select a vehicle condition

condition_options = df['condition'].dropna().unique()

selected_conditions = st.multiselect(
    'Select Vehicle Condition',
    options=condition_options,
    default=condition_options
)

# Apply to the df
filtered_df = df[df['condition'].isin(selected_conditions)]

st.write(f'Number of vehicles selected: {len(filtered_df)}')

# Histogram 
fig_hist = px.histogram(
    filtered_df,
    x='price',
    title='Distribution of Vehicle Prices'
)

st.plotly_chart(fig_hist)

# Scatter plot 
fig_scatter = px.scatter(
    filtered_df,
    x='odometer',
    y='price',
    color='condition',
    title='Vehicle Price vs Mileage by Condition'
)

st.plotly_chart(fig_scatter)
