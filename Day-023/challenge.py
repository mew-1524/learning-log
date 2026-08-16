import numpy as np

marks = np.array([45, 67, 89, 92, 56, 74, 81, 39, 95, 63])

print("Marks:", marks)

print("\nTotal:", np.sum(marks))
print("Average:", np.mean(marks))
print("Highest:", np.max(marks))
print("Lowest:", np.min(marks))

print("\nSorted Marks:", np.sort(marks))

print("\nStudents scoring above 75:")
print(marks[marks > 75])

print("\nStudents scoring below 40:")
print(marks[marks < 40])