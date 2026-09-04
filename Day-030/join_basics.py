import pandas as pd

students = pd.DataFrame({
    "ID": [1, 2, 3, 4],
    "Name": ["Aadesh", "Rahul", "Amit", "Riya"]
})

marks = pd.DataFrame({
    "ID": [1, 2, 3, 4],
    "Marks": [85, 78, 92, 88]
})

print("Students:")
print(students)

print("\nMarks:")
print(marks)

#inner join
result = pd.merge(
    students,
    marks,
    on="ID",
    how="inner"
)