

import pandas as pd

df = pd.read_csv("sales.csv")

print(df)

result = df.groupby("City")["Sales"].agg(
    ["sum", "mean", "max", "min", "count"]
)

print(result)
#new column for revenue
df["Revenue"] = df["Sales"] * df["Quantity"]

print(df)