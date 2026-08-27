import pandas as pd

data = {
    "Name": ["Aadesh", "Rahul", "Amit", "Riya", "Neha"],
    "Age": [17, 18, 17, None, 17],
    "Python": [85, 72, 91, None, 95],
    "SQL": [88, 75, 89, 70, None],
    "City": ["Mumbai", "Pune", "Mumbai", "Nashik", "Mumbai"]
}

df = pd.DataFrame(data)

print("ORIGINAL DATA")
print(df)

print("\nMISSING VALUES")
print(df.isnull().sum())

# Fill missing numerical values
df["Age"] = df["Age"].fillna(df["Age"].mean())
df["Python"] = df["Python"].fillna(df["Python"].mean())
df["SQL"] = df["SQL"].fillna(df["SQL"].mean())

print("\nCLEANED DATA")
print(df)

print("\nPYTHON > 80")
print(df[df["Python"] > 80])

print("\nSORTED BY PYTHON")
print(df.sort_values("Python", ascending=False))