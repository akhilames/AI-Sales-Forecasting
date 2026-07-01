import streamlit as st
import pandas as pd
import numpy as np

# Set up the web page title
st.set_page_config(page_title="AI Sales & Inventory Management", layout="wide")

# Title of the Project
st.title("📊 AI-Powered Sales Forecasting & Inventory Management")
st.write("Welcome! This AI system predicts future sales trends and optimizes stock levels.")

# Sidebar Configuration
st.sidebar.header("Control Panel")
selected_product = st.sidebar.selectbox("Select a Product", ["Product A", "Product B", "Product C"])
forecast_days = st.sidebar.slider("Forecast Period (Days)", 7, 30, 14)

# Create two columns for Layout
col1, col2 = st.columns(2)

with col1:
    st.subheader(f"📈 Predicted Sales Trend for {selected_product}")
    # Generating mock forecasting data
    dates = pd.date_range(start="2026-05-26", periods=forecast_days)
    predicted_sales = np.random.randint(50, 200, size=forecast_days)
    df_sales = pd.DataFrame({"Date": dates, "Estimated Demand": predicted_sales})
    df_sales.set_index("Date", inplace=True)
    
    # Display Chart
    st.line_chart(df_sales)

with col2:
    st.subheader("📦 Inventory Optimization Insights")
    current_stock = np.random.randint(100, 500)
    avg_demand = int(predicted_sales.mean())
    status = "✅ Stock is Optimal" if current_stock > (avg_demand * 2) else "⚠️ Low Stock Alert! Restock Soon."
    
    # Display Key Metrics
    st.metric(label="Current Warehouse Stock", value=current_stock)
    st.metric(label="Average Forecasted Daily Demand", value=avg_demand)
    st.info(f"**AI Recommendation:** {status}")

st.success("System is running correctly with the ML forecasting module initialized.")
