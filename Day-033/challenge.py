import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("sales.csv")

product_sales = df.groupby("Product")["Sales"].sum()

plt.bar(
    product_sales.index,
    product_sales.values
)

plt.title("Sales by Product")
plt.xlabel("Product")
plt.ylabel("Sales")

plt.xticks(rotation=45)

plt.show()