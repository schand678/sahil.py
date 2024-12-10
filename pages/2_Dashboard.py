import streamlit as st
import pandas as pd

# Title
st.title("Read a CSV File Directly in Streamlit")

# Path to the CSV file
file_path = "clusterst__rows.csv"  # Replace with your CSV file path

# Read the CSV file
try:
    df = pd.read_csv(file_path)
    
    # Display the dataframe
    st.write("Here is the content of your CSV file:")
    st.dataframe(df)
except FileNotFoundError:
    st.error(f"File not found at the specified path: {file_path}")

