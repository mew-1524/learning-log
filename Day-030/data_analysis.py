import pandas as pd

students = pd.DataFrame({
    "ID": [1, 2, 3, 4, 5],
    "Name": ["Aadesh", "Rahul", "Amit", "Riya", "Neha"],
    "Department": ["IT", "IT", "CS", "CS", "IT"]
})

marks = pd.DataFrame({
    "ID": [1, 2, 3, 4, 5],
    "Python": [85, 78, 92, 88, 75],
    "SQL": [90, 80, 89, 85, 82]
})

df = pd.merge(
    students,
    marks,
    on="ID"
)

print("Complete Data:")
print(df)

df["Total"] = df["Python"] + df["SQL"]

df["Average"] = df["Total"] / 2

print("\nFinal Data:")
print(df)

print("\nTop Student:")

top_student = df.loc[
    df["Average"].idxmax()
]

print(top_student)