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


except FileNotFoundError:
    st.error(f"File not found at: {file_path}. Please ensure the file is in the correct location.")

except Exception as e:
    st.error(f"An unexpected error occurred: {e}")



# Average Price per Cluster
if 'price' in data.columns:
    st.write("### Average Price per Cluster")
    avg_price_per_cluster = data.groupby('Cluster')['price'].mean().reset_index()
    st.write(avg_price_per_cluster)  # Debugging: Ensure the data is aggregated correctly

  
else:
    st.warning("The column 'price' is required for this chart, but it is missing.")


# Sidebar for cluster selection
st.sidebar.header("Filter Options")
selected_clusters = st.sidebar.multiselect(
    "Select Clusters to Display",
    options=data['Cluster'].unique(),
    default=data['Cluster'].unique()
)

# Filter data based on selection
filtered_data = data[data['Cluster'].isin(selected_clusters)]
st.write(f"### Filtered Data Preview ({len(filtered_data)} rows)")
st.dataframe(filtered_data)



