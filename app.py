# Load data function
@st.cache_data
def load_data(file):
    """Load the dataset and cache it for performance."""
    df = pd.read_csv(file)
    # Rename columns to uppercase
    df.columns = [col.upper() for col in df.columns]
    return df

# Main logic remains the same
if uploaded_file is not None:
    st.sidebar.success("📂 File uploaded successfully!")
    df = load_data(uploaded_file)

    st.write("### Dataset Preview")
    st.dataframe(df.head(), use_container_width=True)

    # Check if necessary columns are present (in uppercase now)
    if {'MAKE', 'PRICE', 'CLUSTER', 'MILEAGE', 'STOCK_TYPE'}.issubset(df.columns):
        # Input Section
        st.sidebar.header("📊 Input Parameters")
        input_make = st.sidebar.selectbox("Select Vehicle Make", df['MAKE'].unique())
        input_price = st.sidebar.number_input("Enter Vehicle Price ($)", min_value=0, value=20000, step=1000)
        input_mileage = st.sidebar.number_input("Enter Vehicle Mileage (km)", min_value=0, value=50000, step=1000)
        price_tolerance = st.sidebar.slider("Price Tolerance ($)", min_value=500, max_value=10000, value=2000, step=500)
        mileage_tolerance = st.sidebar.slider("Mileage Tolerance (km)", min_value=1000, max_value=20000, value=5000, step=1000)
        top_n = st.sidebar.slider("Number of Recommendations", min_value=1, max_value=20, value=5)

        # Get Recommendations
        if st.sidebar.button("💡 Get Recommendations"):
            recommendations = recommend_by_cluster_price_and_mileage(
                input_make, input_price, input_mileage, df,
                cluster_column='CLUSTER', price_tolerance=price_tolerance,
                mileage_tolerance=mileage_tolerance, top_n=top_n
            )

            # Check recommendations
            if recommendations.empty:
                st.warning("No exact matches found. Expanding search criteria...")

                # Step 1: Loosen tolerances
                expanded_recommendations = df[
                    (df['PRICE'] >= input_price - 2 * price_tolerance) &
                    (df['PRICE'] <= input_price + 2 * price_tolerance) &
                    (df['MILEAGE'] >= input_mileage - 2 * mileage_tolerance) &
                    (df['MILEAGE'] <= input_mileage + 2 * mileage_tolerance)
                ]

                # Step 2: Compute 'combined_difference' for expanded dataset
                if not expanded_recommendations.empty:
                    expanded_recommendations['combined_difference'] = (
                        abs(expanded_recommendations['PRICE'] - input_price) +
                        abs(expanded_recommendations['MILEAGE'] - input_mileage)
                    )
                    expanded_recommendations = expanded_recommendations.sort_values(by='combined_difference').head(top_n)
                    st.success("Here are matches with expanded tolerances:")
                    st.dataframe(expanded_recommendations)
                else:
                    # Step 3: Fallback - Show top cars from the dataset
                    st.warning("Still no matches found. Showing general recommendations:")
                    fallback_recommendations = df.copy()

                    # Calculate 'combined_difference' for the full dataset
                    fallback_recommendations['combined_difference'] = (
                        abs(fallback_recommendations['PRICE'] - input_price) +
                        abs(fallback_recommendations['MILEAGE'] - input_mileage)
                    )
                    fallback_recommendations = fallback_recommendations.sort_values(by='combined_difference').head(top_n)
                    st.dataframe(fallback_recommendations)
            else:
                # Show strict recommendations
                st.subheader("📋 Recommendations (Strict Criteria)")
                st.markdown(f"### Recommendations for `{input_make}` near price `${input_price}` and mileage `{input_mileage}`:")
                st.dataframe(recommendations)
    else:
        st.error("⚠️ The dataset must contain the columns: 'MAKE', 'PRICE', 'CLUSTER', 'MILEAGE', and 'STOCK_TYPE'.")
else:
    st.warning("📥 Upload a CSV file to start!")
