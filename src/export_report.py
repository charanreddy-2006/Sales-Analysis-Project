import pandas as pd

# Read dataset
df = pd.read_csv("data/sales.csv")

# Create summary
summary = df.groupby("Category").agg({
    "Sales": "sum",
    "Profit": "sum",
    "Quantity": "sum"
})

# Save CSV
summary.to_csv("reports/category_summary.csv", index=True)

# Save Excel
summary.to_excel("reports/category_summary.xlsx", index=True)

print("Reports exported successfully!")