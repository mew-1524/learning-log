import pandas as pd

df = pd.read_csv("students.csv")

print(df.head())
print(df.tail())
print(df.shape)
print(df.columns)
print(df.info())
print(df.describe())