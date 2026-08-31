import pandas as pd

data = {
    "Employee": [
        "A", "B", "C", "D", "E",
        "F", "G", "H", "I", "J"
    ],

    "Department": [
        "IT", "HR", "IT", "Sales", "HR",
        "IT", "Sales", "HR", "IT", "Sales"
    ],

    "City": [
        "Mumbai", "Pune", "Mumbai", "Pune", "Mumbai",
        "Pune", "Mumbai", "Pune", "Mumbai", "Nashik"
    ],

    "Salary": [
        50000, 45000, 60000, 40000, 55000,
        52000, 48000, 47000, 65000, 42000
    ],

    "Experience": [
        2, 3, 4, 1, 5,
        3, 2, 4, 6, 2
    ]
}

df = pd.DataFrame(data)

print("DATA")
print(df)

print("\nAverage Salary:")
print(df["Salary"].mean())

print("\nTotal Salary:")
print(df["Salary"].sum())

print("\nAverage Salary by Department:")
print(
    df.groupby("Department")["Salary"].mean()
)

print("\nMaximum Salary by Department:")
print(
    df.groupby("Department")["Salary"].max()
)

print("\nEmployees per Department:")
print(
    df.groupby("Department").size()
)

print("\nAverage Experience:")
print(
    df.groupby("Department")["Experience"].mean()
)

print("\nDepartment + City Average Salary:")
print(
    df.groupby(
        ["Department", "City"]
    )["Salary"].mean()
)

print("\nSummary:")
print(
    df.groupby("Department").agg({
        "Salary": ["mean", "max", "min"],
        "Experience": ["mean", "max"]
    })
)

department_salary = (
    df.groupby("Department")["Salary"]
    .mean()
)

print("\nHighest Average Salary Department:")
print(department_salary.idxmax())

city_salary = (
    df.groupby("City")["Salary"]
    .sum()
)

print("\nHighest Total Salary City:")
print(city_salary.idxmax())

print("\nDepartments Sorted by Average Salary:")

result = (
    df.groupby("Department")["Salary"]
    .mean()
    .reset_index()
    .sort_values("Salary", ascending=False)
)

print(result)