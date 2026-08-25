import pandas as pd

students = {
    "Name": ["Aadesh", "Rahul", "Amit", "Riya", "Neha", "Karan"],
    "Python": [85, 72, 91, 68, 95, 78],
    "SQL": [88, 75, 89, 70, 92, 80],
    "Maths": [80, 70, 94, 65, 96, 76]
}

df = pd.DataFrame(students)

print("STUDENT DATA")
print(df)

print("\nShape:")
print(df.shape)

print("\nAverage Python Marks:")
print(df["Python"].mean())

print("\nAverage SQL Marks:")
print(df["SQL"].mean())

print("\nAverage Maths Marks:")
print(df["Maths"].mean())

print("\nStudents with Python marks above 80:")
print(df[df["Python"] > 80])

print("\nTop Maths Marks:")
print(df["Maths"].max())