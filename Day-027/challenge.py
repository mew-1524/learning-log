import pandas as pd

data = {
    "Name": ["A", "B", "C", "D", "E"],
    "Python": [80, 65, 90, 55, 95],
    "SQL": [85, 70, 88, 60, 92],
    "Maths": [78, 75, 95, 58, 90]
}

df = pd.DataFrame(data)

print("Data:")
print(df)

print("\nName and Python:")
print(df[["Name", "Python"]])

print("\nPython Average:")
print(df["Python"].mean())

print("\nHighest SQL Mark:")
print(df["SQL"].max())

print("\nPython > 75:")
print(df[df["Python"] > 75])

df["Average"] = (
    df["Python"] +
    df["SQL"] +
    df["Maths"]
) / 3

print("\nWith Average:")
print(df)

print("\nAverage > 80:")
print(df[df["Average"] > 80])

print("\nTop Student:")
print(df.loc[df["Average"].idxmax()])