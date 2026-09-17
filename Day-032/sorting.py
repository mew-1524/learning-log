import pandas as pd

df = pd.read_csv("sales.csv")

print(df.sort_values("Sales"))

print(df.sort_values("Sales", ascending=False))