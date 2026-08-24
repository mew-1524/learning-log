import numpy as np

students = np.array([
    [80, 75, 90],
    [65, 82, 78],
    [92, 88, 95],
    [70, 85, 80],
    [45, 55, 60],
    [88, 91, 86]
])

print("================================")
print("   STUDENT PERFORMANCE ANALYSIS")
print("================================")

print("\nMarks:")
print(students)

# -------------------------------
# Overall Statistics
# -------------------------------

print("\nOverall Average:")
print(np.mean(students))

print("\nHighest Mark:")
print(np.max(students))

print("\nLowest Mark:")
print(np.min(students))

# -------------------------------
# Student-wise Average
# -------------------------------

student_average = np.mean(students, axis=1)

print("\nStudent-wise Average:")
print(student_average)

# -------------------------------
# Subject-wise Average
# -------------------------------

subject_average = np.mean(students, axis=0)

print("\nSubject-wise Average:")
print(subject_average)

# -------------------------------
# Highest Student Average
# -------------------------------

print("\nHighest Student Average:")
print(np.max(student_average))

# -------------------------------
# Lowest Student Average
# -------------------------------

print("\nLowest Student Average:")
print(np.min(student_average))

# -------------------------------
# Students Above 80
# -------------------------------

top_students = students[student_average >= 80]

print("\nStudents with Average >= 80:")
print(top_students)

# -------------------------------
# Add 5 Bonus Marks
# -------------------------------

updated_marks = students + 5

print("\nAfter Adding 5 Bonus Marks:")
print(updated_marks)