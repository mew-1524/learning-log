import matplotlib.pyplot as plt

days = [1, 2, 3, 4, 5]
sales = [100, 150, 120, 200, 250]

plt.plot(days, sales)

plt.title("Daily Sales")
plt.xlabel("Day")
plt.ylabel("Sales")

plt.show()