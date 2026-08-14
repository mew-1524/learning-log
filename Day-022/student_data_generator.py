import numpy as np

students = 10

marks = np.random.randint(40, 101, students)

print("Student Marks:")
print(marks)

print("\nHighest Marks:", np.max(marks))
print("Lowest Marks:", np.min(marks))
print("Average Marks:", np.mean(marks))
print("Total Marks:", np.sum(marks))