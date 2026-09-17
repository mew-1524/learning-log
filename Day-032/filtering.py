import pandas as pd

df = pd.read_csv("sales.csv")

high_sales = df[df["Sales"] > 10000]

print(high_sales)