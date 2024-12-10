import streamlit as st
import pandas as pd

# Title of the app
st.title("Vehicle Make Clustering: Unlocking Sales Insights")

data = pd.read_csv("clusterst__rows.csv")

st.data.head(10)

