import pandas as pd

data = {
    "Name": ["A", "B", "C", "D", "E", "F"],
    "Age": [18, 17, 19, 18, None, 17],
    "Python": [85, 72, 95, None, 78, 88],
    "SQL": [90, 75, 92, 70, None, 85],
    "City": ["Mumbai", "Pune", "Mumbai", "Nashik", "Pune", "Mumbai"]
}

df = pd.DataFrame(data)

print(df)

print("\nName and Python:")
print(df[["Name", "Python"]])

print("\nPython > 80:")
print(df[df["Python"] > 80])

print("\nMumbai Students:")
print(df[df["City"] == "Mumbai"])

print("\nPython > 80 AND SQL > 80:")
print(
    df[
        (df["Python"] > 80) &
        (df["SQL"] > 80)
    ]
)

print("\nSorted:")
print(df.sort_values("Python", ascending=False))

print("\nMissing Values:")
print(df.isnull().sum())

df["Age"] = df["Age"].fillna(df["Age"].mean())
df["Python"] = df["Python"].fillna(df["Python"].mean())
df["SQL"] = df["SQL"].fillna(df["SQL"].mean())

df["Average"] = (
    df["Python"] + df["SQL"]
) / 2

print("\nCleaned Data:")
print(df)

print("\nAverage > 80:")
print(df[df["Average"] > 80])