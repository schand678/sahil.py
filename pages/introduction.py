import streamlit as st

# Set page configuration
st.set_page_config(page_title="Vehicle Make Clustering",)

# Main Title
st.title("Vehicle Make Clustering: Unlocking Sales Insights")

# Introduction Section
st.subheader("About the Project")
st.write("""
 This initiative leverages data science techniques to analyze 
and group vehicle makes based on their unique attributes and sales performance. The dataset utilized contains 
comprehensive information, including:
- **Vehicle Specifications**: Make, model, year, mileage, and price.
- **Sales Data**: Transaction details from multiple dealerships over a specific timeframe.
""")

# Problem Statement
st.subheader("Understanding the Challenge")
st.write("""
Dealerships often face challenges such as:
- Identifying top-performing vehicle makes.
- Managing inventory efficiently.
- Developing data-backed marketing strategies.

This project aims to address these issues by uncovering patterns in vehicle sales and clustering vehicle makes 
for actionable insights.
""")

# Objectives Section
st.subheader("What We Aim to Achieve")
st.write("""
Our project focuses on the following objectives:
1. Conducting an **Exploratory Data Analysis (EDA)** to identify sales patterns.
2. Building a **Clustering Model** to categorize vehicle makes based on their features.
3. Utilizing the clusters to:
   - Recognize high-demand vehicle categories.
   - Optimize dealership inventory planning.
   - Enhance marketing strategies for better customer engagement.
""")


# Call to Action
st.subheader("Join Us on This Journey")
st.write("""
This project is a step towards innovation in the automotive industry. Let’s harness the power of data to drive 
better business outcomes and revolutionize how dealerships operate!
""")
