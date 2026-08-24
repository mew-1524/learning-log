import numpy as np

marks = np.array([45, 67, 89, 32, 91, 56, 76, 84])

passed = marks[marks >= 40]

print("Passed Students:")
print(passed)

failed = marks[marks < 40]

print("\nFailed Students:")
print(failed)

excellent = marks[marks >= 80]

print("\nExcellent Students:")
print(excellent)