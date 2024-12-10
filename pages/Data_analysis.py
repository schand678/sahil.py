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

import streamlit as st
import pandas as pd
import plotly.express as px

# Title
st.title("🚗 Vehicle Data Visualizations")

# File path (replace if necessary)
file_path = "./clean_data.csv"

# Load data
try:
    data = pd.read_csv(file_path)

    # Display the first few rows
    st.subheader("Dataset Preview")
    st.dataframe(data.head())

    # Cluster Distribution
    st.subheader("📊 Cluster Distribution")
    cluster_counts = data['Cluster'].value_counts().reset_index()
    cluster_counts.columns = ['Cluster', 'Count']
    fig_cluster_dist = px.bar(
        cluster_counts,
        x='Cluster',
        y='Count',
        text='Count',
        title="Number of Entries per Cluster"
    )
    st.plotly_chart(fig_cluster_dist)

    # Scatter Plot: Price vs. Mileage
    st.subheader("📈 Price vs. Mileage")
    fig_price_mileage = px.scatter(
        data,
        x='mileage',
        y='price',
        color='Cluster',
        hover_data=['make', 'model', 'model_year'],
        title="Price vs. Mileage Colored by Cluster",
        labels={"mileage": "Mileage", "price": "Price ($)"}
    )
    st.plotly_chart(fig_price_mileage)

    # Average Price per Cluster
    st.subheader("💵 Average Price per Cluster")
    avg_price_cluster = data.groupby('Cluster')['price'].mean().reset_index()
    fig_avg_price = px.bar(
        avg_price_cluster,
        x='Cluster',
        y='price',
        text='price',
        title="Average Price by Cluster",
        labels={"price": "Average Price ($)"}
    )
    st.plotly_chart(fig_avg_price)

except FileNotFoundError:
    st.error(f"File not found at: {file_path}. Please ensure the file is in the correct location.")

