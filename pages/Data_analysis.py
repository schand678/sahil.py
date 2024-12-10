import streamlit as st
import pandas as pd
import plotly.express as px

# Title
st.title("🚗 Cluster Distribution Visualization")

# File path (replace with your actual file path if needed)
file_path = "./clean_data.csv"

# Load data
try:
    data = pd.read_csv(file_path)

    # Display the first few rows
    st.subheader("Dataset Preview")
    st.dataframe(data.head())

    # Cluster Distribution Visualization
    st.subheader("📊 Cluster Distribution")
    cluster_counts = data['Cluster'].value_counts().reset_index()
    cluster_counts.columns = ['Cluster', 'Count']
    fig_cluster_dist = px.bar(
        cluster_counts,
        x='Cluster',
        y='Count',
        text='Count',
        title="Number of Entries per Cluster",
        labels={"Count": "Number of Vehicles", "Cluster": "Cluster ID"}
    )
    st.plotly_chart(fig_cluster_dist)

except FileNotFoundError:
    st.error(f"File not found at: {file_path}. Please ensure the file is in the correct location.")

except Exception as e:
    st.error(f"An unexpected error occurred: {e}")
