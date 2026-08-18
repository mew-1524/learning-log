import numpy as np

sales = np.array([
    [20, 25, 30, 22, 28],
    [15, 18, 20, 25, 30],
    [30, 28, 35, 32, 40]
])

print("Sales Data:")
print(sales)

print("\nTotal Sales:", np.sum(sales))

print("\nProduct-wise Sales:")
print(np.sum(sales, axis=1))

print("\nDay-wise Sales:")
print(np.sum(sales, axis=0))

print("\nHighest Sale:", np.max(sales))

print("\nLowest Sale:", np.min(sales))

print("\nAverage Sale:", np.mean(sales))