import streamlit as st
import pandas as pd

# Title
st.title("📊 Basic Cluster Distribution Visualization")

# File path (update if necessary)
file_path = "./clean_data.csv"

try:
    # Load data
    data = pd.read_csv(file_path)

    # Display the dataset
    st.write("### Dataset Preview")
    st.write(data.head())

    # Verify the 'Cluster' column exists
    if 'Cluster' not in data.columns:
        st.error("The 'Cluster' column is missing in the dataset!")
    else:
        # Count the occurrences of each cluster
        cluster_counts = data['Cluster'].value_counts()

        # Display the counts as a table
        st.write("### Cluster Counts")
        st.write(cluster_counts)

        # Create a simple bar chart using Streamlit
        st.bar_chart(cluster_counts)

except FileNotFoundError:
    st.error(f"File not found at: {file_path}. Please ensure the file is in the correct location.")

except Exception as e:
    st.error(f"An unexpected error occurred: {e}")

