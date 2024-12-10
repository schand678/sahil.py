import streamlit as st
import pandas as pd

# Title of the app
st.title("Vehicle Make Clustering: Unlocking Sales Insights")

# URL of the CSV file in your GitHub repository


try:
    # Read the CSV file from GitHub
    data = pd.read_csv("clusterst__rows.csv")
    
    # Display the first 10 rows
    st.subheader("First 10 Rows of the Dataset")
    st.write(data.head(10))
except Exception as e:
    st.error(f"Error loading data: {e}")
