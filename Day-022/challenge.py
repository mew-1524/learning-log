import numpy as np

numbers = np.arange(1, 21)

print("Original:")
print(numbers)

# Reshape into 4 rows and 5 columns
matrix = numbers.reshape(4, 5)

print("\nMatrix:")
print(matrix)

print("\nMaximum:", np.max(matrix))
print("Minimum:", np.min(matrix))
print("Mean:", np.mean(matrix))