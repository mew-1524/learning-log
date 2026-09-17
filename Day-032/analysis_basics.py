import pandas as pd

df = pd.read_csv("sales.csv")

print(df)

print("Total Sales:", df["Sales"].sum())
print("Average Sales:", df["Sales"].mean())
print("Maximum Sale:", df["Sales"].max())
print("Minimum Sale:", df["Sales"].min())
print("Number of Orders:", df["OrderID"].count())