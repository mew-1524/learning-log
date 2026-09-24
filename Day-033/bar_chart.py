import matplotlib.pyplot as plt

cities = ["Mumbai", "Pune", "Delhi"]
sales = [65000, 16200, 78000]

plt.bar(cities, sales)

plt.title("Sales by City")
plt.xlabel("City")
plt.ylabel("Sales")

plt.show()