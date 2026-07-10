import pandas as pd

# Read the dataset
df = pd.read_csv("data/sales.csv")

print("========== SALES ANALYSIS ==========\n")

print("Total Orders :", len(df))
print("Total Sales  :", df["Sales"].sum())
print("Total Profit :", df["Profit"].sum())
print("Average Sale :", df["Sales"].mean())
print("Highest Sale :", df["Sales"].max())
print("Lowest Sale  :", df["Sales"].min())

print("\nSales by Category")
print(df.groupby("Category")["Sales"].sum())

print("\nProfit by Region")
print(df.groupby("Region")["Profit"].sum())

print("\nQuantity by Category")
print(df.groupby("Category")["Quantity"].sum())