import streamlit as st
import pandas as pd

# Set up Streamlit app
st.title("📂 Direct File Load")

# Load data directly from the file
file_path = "./clean_data.csv"  # Update this to the correct file path if not in the same directory

try:
    data = pd.read_csv(file_path)

    # Display the first few rows of the dataset
    st.subheader("Loaded Data Preview")
    st.write(data.head())

    # Show column names for verification
    st.write("Columns in the dataset:")
    st.write(data.columns.tolist())

except FileNotFoundError:
    st.error(f"File not found at: {file_path}. Please ensure the file is in the correct location.")
