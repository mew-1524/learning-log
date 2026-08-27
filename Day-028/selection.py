import pandas as pd

data = {
    "Name": ["Aadesh", "Rahul", "Amit", "Riya", "Neha", "Karan"],
    "Age": [17, 18, 17, 18, 17, 19],
    "Python": [85, 72, 91, 68, 95, 76],
    "SQL": [88, 75, 89, 70, 92, 80],
    "City": ["Mumbai", "Pune", "Mumbai", "Nashik", "Mumbai", "Pune"]
}

df = pd.DataFrame(data)

print(df)

print(df["Name"])

print(df[["Name", "Python"]])

print(df.iloc[0])

print(df.iloc[0:3])

print(df.loc[0])

print(df.loc[0, "Python"])