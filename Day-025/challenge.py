import numpy as np

a = np.array([10, 20, 30])
b = np.array([40, 50, 60])

# Combine arrays
combined = np.concatenate((a, b))

print("Combined:")
print(combined)

# Split array
parts = np.split(combined, 2)

print("\nSplit:")
print(parts)

# Add bonus
result = combined + 10

print("\nAfter Bonus:")
print(result)

# Find values greater than 50
filtered = result[result > 50]

print("\nValues greater than 50:")
print(filtered)