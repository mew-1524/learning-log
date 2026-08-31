import pandas as pd

data = {
    "Name": [
        "Aadesh", "Rahul", "Amit", "Riya",
        "Neha", "Karan", "Sneha", "Vijay"
    ],
    "Department": [
        "IT", "HR", "IT", "Sales",
        "HR", "IT", "Sales", "HR"
    ],
    "City": [
        "Mumbai", "Pune", "Mumbai", "Nashik",
        "Mumbai", "Pune", "Mumbai", "Pune"
    ],
    "Salary": [
        50000, 45000, 60000, 40000,
        55000, 52000, 48000, 47000
    ],
    "Experience": [
        2, 3, 4, 1, 5, 3, 2, 4
    ]
}

df = pd.DataFrame(data)

print(df)

df.groupby("Department")["Salary"].mean()

df.groupby("column")["value_column"].operation()

df.groupby("Department")["Salary"].mean()

df.groupby("Department")["Salary"].sum()

df.groupby("Department")["Salary"].max()

df.groupby("Department")["Salary"].min()

result = df.groupby("Department").agg({
    "Salary": "mean",
    "Experience": "max"
})

print(result)

result2 = df.groupby("Department").agg({
    "Salary": ["mean", "max", "min"],
    "Experience": ["mean", "max"]
})

print(result2)

result = df.groupby(
    ["Department", "City"]
)["Salary"].mean()

print(result)
