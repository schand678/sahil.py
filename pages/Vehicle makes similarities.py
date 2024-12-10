import streamlit as st

# Set page configuration
st.set_page_config(
    page_title="Vehicle Make Clustering",
    page_icon=None,  # No car icon as requested
    layout="wide",
)

# Main Title
st.title("🚀 Vehicle Make Clustering: Unlocking Sales Insights")

# Sidebar for Navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio(
    "Go to",
    ("Introduction", "Problem Statement", "Objectives", "Your Input"),
)

# Introduction Section
if page == "Introduction":
    st.subheader("About the Project")
    st.write("""
    This initiative leverages data science techniques to analyze 
    and group vehicle makes based on their unique attributes and sales performance. The dataset utilized contains 
    comprehensive information, including:
    - **Vehicle Specifications**: Make, model, year, mileage, and price.
    - **Sales Data**: Transaction details from multiple dealerships over a specific timeframe.
    """)
    st.info("🔍 Use this section to understand the scope and purpose of the project.")

# Problem Statement
elif page == "Problem Statement":
    st.subheader("Understanding the Challenge")
    st.write("""
    Dealerships often face challenges such as:
    - Identifying top-performing vehicle makes.
    - Managing inventory efficiently.
    - Developing data-backed marketing strategies.

    This project aims to address these issues by uncovering patterns in vehicle sales and clustering vehicle makes 
    for actionable insights.
    """)
    st.success("🌟 Learn about the key challenges that motivated this project.")

# Objectives Section
elif page == "Objectives":
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
    st.warning("⚡ Dive into the project goals to see what we're working towards.")

# Interactive Section for User Input
elif page == "Your Input":
    st.subheader("We Value Your Input")
    st.write("Provide your thoughts and help shape the future of this project!")
    
    feedback = st.text_area("Share your feedback or ideas here:")
    if st.button("Submit Feedback"):
        if feedback.strip():
            st.success("Thank you for your feedback! 🙌")
        else:
            st.error("Please enter some feedback before submitting.")
    
    st.write("### Quick Poll")
    poll_choice = st.radio(
        "Which aspect of the project excites you the most?",
        ("Data Analysis", "Clustering Models", "Sales Insights", "Business Applications"),
    )
    st.write(f"🎯 You selected: **{poll_choice}**")

st.sidebar.info("Navigate through the sections to learn more about the project.")

