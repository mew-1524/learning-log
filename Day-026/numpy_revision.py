import numpy as np

marks = np.array([65, 72, 88, 91, 55, 79])

print("Marks:")
print(marks)

print("\nShape:", marks.shape)
print("Size:", marks.size)
print("Dimensions:", marks.ndim)

print("\nFirst mark:", marks[0])
print("Last mark:", marks[-1])

print("\nFirst three marks:", marks[:3])

print("\nHighest:", np.max(marks))
print("Lowest:", np.min(marks))
print("Average:", np.mean(marks))
print("Total:", np.sum(marks))