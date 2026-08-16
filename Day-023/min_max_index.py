import numpy as np

marks = np.array([72, 91, 65, 88, 95, 79])

print("Marks:", marks)

print("Minimum:", np.min(marks))
print("Minimum Index:", np.argmin(marks))

print("Maximum:", np.max(marks))
print("Maximum Index:", np.argmax(marks))