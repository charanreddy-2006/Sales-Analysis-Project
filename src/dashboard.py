import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Page title
st.set_page_config(page_title="Sales Dashboard", layout="wide")

st.title("📊 Sales Analysis Dashboard")

# Load data
df = pd.read_csv("data/sales.csv")

# Show data
st.header("Sales Dataset")
st.dataframe(df)

# KPI Metrics
total_sales = df["Sales"].sum()
total_profit = df["Profit"].sum()
total_orders = len(df)
average_sales = df["Sales"].mean()

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Sales", f"${total_sales}")
col2.metric("Total Profit", f"${total_profit}")
col3.metric("Orders", total_orders)
col4.metric("Average Sale", f"${average_sales:.2f}")

st.divider()

# Sales by Category
st.subheader("Sales by Category")

sales_category = df.groupby("Category")["Sales"].sum()

fig, ax = plt.subplots(figsize=(6,4))

sns.barplot(
    x=sales_category.index,
    y=sales_category.values,
    hue=sales_category.index,
    palette="viridis",
    legend=False,
    ax=ax
)

ax.set_xlabel("Category")
ax.set_ylabel("Sales")

st.pyplot(fig)

# Profit by Region
st.subheader("Profit by Region")

profit_region = df.groupby("Region")["Profit"].sum()

fig2, ax2 = plt.subplots(figsize=(6,6))

ax2.pie(
    profit_region,
    labels=profit_region.index,
    autopct="%1.1f%%",
    startangle=90
)

st.pyplot(fig2)

# Profit Distribution
st.subheader("Profit Distribution")

fig3, ax3 = plt.subplots(figsize=(8,4))

sns.histplot(df["Profit"], bins=5, color="green", ax=ax3)

st.pyplot(fig3)

# Summary Table
st.subheader("Category Summary")

summary = df.groupby("Category").agg({
    "Sales":"sum",
    "Profit":"sum",
    "Quantity":"sum"
})

st.dataframe(summary)