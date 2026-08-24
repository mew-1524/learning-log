import numpy as np

marks = np.array([
    [78, 85, 90],
    [65, 70, 72],
    [92, 95, 89],
    [55, 60, 58],
    [88, 84, 91]
])

print("Overall Average:", np.mean(marks))

print("Highest Mark:", np.max(marks))

print("Lowest Mark:", np.min(marks))

student_average = np.mean(marks, axis=1)
print("Student Averages:", student_average)

subject_average = np.mean(marks, axis=0)
print("Subject Averages:", subject_average)

top_students = marks[student_average > 80]
print("Students above 80:")
print(top_students)

bonus_marks = marks + 5
print("After Bonus:")
print(bonus_marks)

high_marks = marks[marks > 90]
print("Marks greater than 90:")
print(high_marks)