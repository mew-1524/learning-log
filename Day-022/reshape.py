import numpy as np

arr = np.arange(1, 13)

print("Original:")
print(arr)

new_arr = arr.reshape(3, 4)

print("\nReshaped:")
print(new_arr)