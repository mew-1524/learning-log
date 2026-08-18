import numpy as np

marks = np.array([
    [80, 75, 90],
    [65, 82, 78],
    [92, 88, 95],
    [70, 85, 80]
])

print("Marks:")
print(marks)

print("\nShape:", marks.shape)

print("\nHighest Mark:", np.max(marks))

print("\nColumn-wise Maximum:")
print(np.max(marks, axis=0))

print("\nRow-wise Maximum:")
print(np.max(marks, axis=1))

print("\nColumn-wise Average:")
print(np.mean(marks, axis=0))

print("\nStudent-wise Average:")
print(np.mean(marks, axis=1))