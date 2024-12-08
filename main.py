import streamlit as st 
import plotly.express as px 
import pandas as pd

# Importing the data
df = pd.read_csv('happy.csv')

# User Input
st.title('In Search for Happiness')
x_axis = st.selectbox('Select the data for the X-axis', options=['GDP', 'Happiness', 'Generosity'])
y_axis = st.selectbox('Select the data for the Y-axis', options=['GDP', 'Happiness', 'Generosity'])
st.subheader(f'{x_axis} and {y_axis}')

# Processing the data
x_axis_lower = x_axis.lower()
y_axis_lower = y_axis.lower()

# Displaying the data
fig = px.scatter(x=df[x_axis_lower], y=df[y_axis_lower], labels={'x': f'{x_axis}', 'y': f'{y_axis}'})
st.plotly_chart(fig)
