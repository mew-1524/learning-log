import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("sales.csv")

city_sales = df.groupby("City")["Sales"].sum()

plt.bar(city_sales.index, city_sales.values)

plt.title("Total Sales by City")
plt.xlabel("City")
plt.ylabel("Sales")

plt.show()