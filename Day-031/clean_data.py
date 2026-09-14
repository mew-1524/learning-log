import pandas as pd

df = pd.read_csv("students.csv")

df["Age"] = df["Age"].fillna(df["Age"].mean())
df["Python"] = df["Python"].fillna(df["Python"].mean())
df["SQL"] = df["SQL"].fillna(df["SQL"].mean())

df = df.drop_duplicates()

print(df)
print(df.isnull().sum())