import streamlit as st
import pandas as pd
import plotly.express as px


# Page configuration
st.set_page_config(
    page_title="Sales Dashboard",
    layout="wide"
)


# Title
st.title("📊 Sales Analysis Dashboard")


# Load dataset
df = pd.read_csv("data/sales.csv")


# Show data
st.subheader("Sales Data")
st.dataframe(df)


# Calculate KPIs
total_sales = df["Sales"].sum()
total_profit = df["Profit"].sum()
total_orders = len(df)
average_sales = df["Sales"].mean()


# KPI cards
col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Sales", total_sales)
col2.metric("Total Profit", total_profit)
col3.metric("Total Orders", total_orders)
col4.metric("Average Sale", round(average_sales, 2))


st.divider()


# Sales by Category
st.subheader("Sales by Category")

category_sales = (
    df.groupby("Category")["Sales"]
    .sum()
    .reset_index()
)

fig1 = px.bar(
    category_sales,
    x="Category",
    y="Sales",
    color="Category",
    title="Sales by Category"
)

st.plotly_chart(fig1)


# Sales by Region
st.subheader("Sales by Region")

region_sales = (
    df.groupby("Region")["Sales"]
    .sum()
    .reset_index()
)

fig2 = px.pie(
    region_sales,
    names="Region",
    values="Sales",
    title="Sales Distribution by Region"
)

st.plotly_chart(fig2)


# Summary
st.subheader("Category Summary")

summary = df.groupby("Category").agg(
    {
        "Sales": "sum",
        "Profit": "sum",
        "Quantity": "sum"
    }
)

st.dataframe(summary)