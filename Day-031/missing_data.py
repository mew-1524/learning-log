import pandas as pd

df = pd.read_csv("students.csv")

print(df.isnull())
print(df.isnull().sum())