import numpy as np

original = np.array([10, 20, 30])

copy = original.copy()

copy[0] = 100

print("Original:", original)
print("Copy:", copy)


#view
original = np.array([10, 20, 30])

view = original.view()

view[0] = 100

print("Original:", original)
print("View:", view)