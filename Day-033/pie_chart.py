import matplotlib.pyplot as plt

categories = ["Electronics", "Furniture"]
sales = [127200, 36500]

plt.pie(
    sales,
    labels=categories,
    autopct="%1.1f%%"
)

plt.title("Sales by Category")

plt.show()