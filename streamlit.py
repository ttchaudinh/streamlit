import streamlit as st
import pandas as pd
import altair as alt

# Load the iris dataset
iris = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv")

# Define the sidebar
st.sidebar.header("Iris dataset explorer")
x_axis = st.sidebar.selectbox("X-axis", iris.columns[:-1])
y_axis = st.sidebar.selectbox("Y-axis", iris.columns[:-1])
color = st.sidebar.selectbox("Color", iris.columns[:-1])

# Define the scatter plot
scatter_plot = alt.Chart(iris).mark_circle(size=60).encode(
    x=x_axis,
    y=y_axis,
    color=color,
    tooltip=['species']
).interactive()

# Define the histogram
histogram = alt.Chart(iris).mark_bar().encode(
    x=alt.X(x_axis, bin=alt.Bin(maxbins=30)),
    y='count()',
    color=color,
    tooltip=['species']
).interactive()

# Define the chart area
chart_area = alt.hconcat(scatter_plot, histogram)

# Define the app layout
st.title("Iris dataset explorer")
st.write("This app allows you to explore the famous iris dataset.")
st.sidebar.markdown("### Scatter plot settings")
st.altair_chart(chart_area, use_container_width=True)
