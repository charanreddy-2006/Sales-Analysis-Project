import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("data/sales.csv")

sales = df.groupby("Category", as_index=False)["Sales"].sum()

plt.figure(figsize=(8,5))

sns.barplot(
    data=sales,
    x="Category",
    y="Sales",
    hue="Category",
    palette="viridis",
    legend=False
)

plt.title("Sales by Category")

plt.savefig("reports/sales_by_category.png")
plt.show()