import streamlit as st
import pandas as pd
import plotly.express as px

# Set page configuration
st.set_page_config(page_title="Clustering Insights", layout="wide")

# Title
st.title("🔍 Vehicle Clustering Insights")

# Load Data
@st.cache_data
def load_data(file_path):
    return pd.read_csv(file_path)

data = load_data('/mnt/data/clean_data.csv')

# Sidebar Filters
st.sidebar.header("Filter Options")
available_clusters = data['Cluster'].unique()
selected_clusters = st.sidebar.multiselect(
    "Select Clusters to Visualize",
    options=available_clusters,
    default=available_clusters
)

# Filter data by selected clusters
filtered_data = data[data['Cluster'].isin(selected_clusters)]

# Display filtered data
st.subheader("Filtered Data")
st.dataframe(filtered_data)

# Cluster Distribution
st.subheader("Cluster Distribution")
if 'price' in filtered_data.columns and 'mileage' in filtered_data.columns:
    scatter_fig = px.scatter(
        filtered_data,
        x='mileage',
        y='price',
        color='Cluster',
        hover_data=['make', 'model', 'model_year'],
        title="Price vs Mileage by Cluster",
        labels={"mileage": "Mileage", "price": "Price ($)"}
    )
    st.plotly_chart(scatter_fig)

# Cluster Counts
st.subheader("Cluster Counts")
cluster_counts = filtered_data['Cluster'].value_counts().reset_index()
cluster_counts.columns = ['Cluster', 'Count']
bar_fig = px.bar(
    cluster_counts,
    x='Cluster',
    y='Count',
    text='Count',
    title="Number of Vehicles in Each Cluster"
)
st.plotly_chart(bar_fig)

# Average Price per Cluster
if 'price' in filtered_data.columns:
    avg_price = filtered_data.groupby('Cluster')['price'].mean().reset_index()
    price_fig = px.bar(
        avg_price,
        x='Cluster',
        y='price',
        text='price',
        title="Average Price by Cluster",
        labels={"price": "Average Price ($)"}
    )
    st.plotly_chart(price_fig)

# Key Metrics
st.sidebar.header("Key Metrics")
total_clusters = len(filtered_data['Cluster'].unique())
total_vehicles = filtered_data.shape[0]
avg_price_all = filtered_data['price'].mean() if 'price' in filtered_data.columns else 0

st.sidebar.metric("Total Clusters", total_clusters)
st.sidebar.metric("Total Vehicles", total_vehicles)
st.sidebar.metric("Average Price", f"${avg_price_all:,.2f}")
