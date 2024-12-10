import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Title
st.title("📊 Cluster Distribution - Debugging Step")

# File path (update if needed)
file_path = "./clean_data.csv"

try:
    # Load data
    data = pd.read_csv(file_path)
    
    # Debugging: Display dataset structure
    st.write("### Dataset Structure")
    st.write(data.head())  # Display the first 5 rows
    st.write("### Columns in the Dataset")
    st.write(data.columns.tolist())  # Display all column names
    
    # Check if 'Cluster' column exists
    if 'Cluster' not in data.columns:
        st.error("The 'Cluster' column is missing in the dataset!")
    else:
        # Count values for each cluster
        cluster_counts = data['Cluster'].value_counts()

        # Debugging: Show the counts
        st.write("### Cluster Counts")
        st.write(cluster_counts)

        # Create a simple bar chart
        st.write("### Bar Chart of Cluster Distribution")
        fig, ax = plt.subplots()
        cluster_counts.plot(kind='bar', ax=ax, color='skyblue')
        ax.set_title("Number of Entries per Cluster")
        ax.set_xlabel("Cluster")
        ax.set_ylabel("Count")
        st.pyplot(fig)

except FileNotFoundError:
    st.error(f"File not found at: {file_path}. Please ensure the file is in the correct location.")

except Exception as e:
    st.error(f"An unexpected error occurred: {e}")

