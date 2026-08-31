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

result = df.groupby(
    ["Department", "City"]
)["Salary"].mean()

print(result)
