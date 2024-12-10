import streamlit as st
import pandas as pd
import plotly.express as px

# Set page configuration
st.set_page_config(
    page_title="Clustering Insights",
    layout="wide"
)

# Title
st.title("🔍 Clustering Insights")

# Upload Data
st.sidebar.header("Upload Your Data")
uploaded_file = st.sidebar.file_uploader("Upload a CSV file with your clustering data", type="csv")

if uploaded_file:
    try:
        # Load data
        data = pd.read_csv(uploaded_file)
        st.write("### Uploaded Data Preview")
        st.dataframe(data.head())

        # Convert all column names to lowercase except for 'Cluster'
        data.columns = [col if col == "Cluster" else col.lower() for col in data.columns]

        # Debugging Output: Show column names after processing
        st.write("### Processed Column Names")
        st.write(data.columns.tolist())

        # Sidebar Filters
        st.sidebar.subheader("Filters")
        if 'Cluster' not in data.columns:
            st.error("Error: 'Cluster' column is missing in the uploaded dataset.")
        else:
            available_clusters = data['Cluster'].unique()
            selected_cluster = st.sidebar.multiselect(
                "Select Clusters to View",
                options=available_clusters,
                default=available_clusters
            )

            # Filter data
            filtered_data = data[data['Cluster'].isin(selected_cluster)]

            # Display filtered data
            st.subheader("Filtered Data")
            st.dataframe(filtered_data)

            # Visualizations
            st.subheader("Cluster Visualizations")

            # Scatter Plot: Cluster Distribution
            if 'x' in filtered_data.columns and 'y' in filtered_data.columns:
                st.write("### Cluster Distribution")
                fig = px.scatter(
                    filtered_data,
                    x="x",
                    y="y",
                    color="Cluster",
                    hover_data=['make', 'model'] if 'make' in filtered_data.columns and 'model' in filtered_data.columns else None,
                    title="Cluster Distribution"
                )
                st.plotly_chart(fig)
            else:
                st.warning("Scatter plot not shown. Columns 'x' and 'y' are missing.")

            # Bar Chart: Count per Cluster
            st.write("### Count of Vehicles per Cluster")
            cluster_counts = filtered_data['Cluster'].value_counts().reset_index()
            cluster_counts.columns = ['Cluster', 'Count']
            fig = px.bar(
                cluster_counts,
                x="Cluster",
                y="Count",
                title="Number of Vehicles in Each Cluster",
                text="Count"
            )
            st.plotly_chart(fig)

            # Average Price per Cluster
            if 'price' in filtered_data.columns:
                st.write("### Average Price per Cluster")
                avg_price = filtered_data.groupby('Cluster')['price'].mean().reset_index()
                fig = px.bar(
                    avg_price,
                    x="Cluster",
                    y="price",
                    title="Average Price by Cluster",
                    text="price"
                )
                st.plotly_chart(fig)
            else:
                st.warning("Average price visualization not shown. 'price' column is missing.")

            # Insights
            st.subheader("Key Insights")
            total_clusters = len(filtered_data['Cluster'].unique())
            st.metric("Total Clusters", total_clusters)
            st.metric("Total Vehicles", filtered_data.shape[0])
            if 'price' in filtered_data.columns:
                avg_price_overall = filtered_data['price'].mean()
                st.metric("Average Price Overall", f"${avg_price_overall:,.2f}")

    except Exception as e:
        st.error(f"An error occurred while processing your data: {e}")

else:
    st.write("Please upload a CSV file to visualize clustering insights.")

