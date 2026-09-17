import pandas as pd

df = pd.read_csv("sales.csv")

print("DATA")
print(df)

print("\nTOTAL SALES")
print(df["Sales"].sum())

print("\nAVERAGE SALES")
print(df["Sales"].mean())

print("\nHIGHEST SALE")
print(df["Sales"].max())

print("\nLOWEST SALE")
print(df["Sales"].min())

print("\nSALES BY CITY")
print(df.groupby("City")["Sales"].sum())

print("\nSALES BY CATEGORY")
print(df.groupby("Category")["Sales"].sum())

print("\nTOP 5 SALES")
print(df.sort_values("Sales", ascending=False).head())

print("\nELECTRONICS SALES")
print(df[df["Category"] == "Electronics"])

df["Revenue"] = df["Sales"] * df["Quantity"]

print("\nDATA WITH REVENUE")
print(df)