import numpy as np

students = np.array([
    [80, 75, 90],
    [65, 82, 78],
    [92, 88, 95],
    [70, 85, 80]
])

print("Original Marks:")
print(students)

# Add 5 bonus marks to every subject
updated = students + 5

print("\nAfter Bonus:")
print(updated)

# Find average marks of each student
average = np.mean(updated, axis=1)

print("\nStudent Averages:")
print(average)

# Students whose average is greater than 85
top_students = updated[average > 85]

print("\nStudents with average above 85:")
print(top_students)