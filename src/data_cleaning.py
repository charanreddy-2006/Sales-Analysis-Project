import pandas as pd

df = pd.read_csv("data/sales.csv")

# Remove duplicate rows
df = df.drop_duplicates()

print(df)