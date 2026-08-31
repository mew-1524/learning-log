import pandas as pd

data = {
    "Product": [
        "Laptop", "Phone", "Laptop", "Tablet",
        "Phone", "Laptop", "Tablet", "Phone"
    ],

    "Category": [
        "Electronics", "Electronics", "Electronics",
        "Electronics", "Electronics", "Electronics",
        "Electronics", "Electronics"
    ],

    "City": [
        "Mumbai", "Pune", "Mumbai", "Nashik",
        "Mumbai", "Pune", "Mumbai", "Pune"
    ],

    "Sales": [
        80000, 50000, 90000, 40000,
        55000, 75000, 45000, 60000
    ]
}

df = pd.DataFrame(data)

print("SALES DATA")
print(df)

print("\nTotal Sales:")
print(df["Sales"].sum())

print("\nSales by Product:")
print(
    df.groupby("Product")["Sales"].sum()
)

print("\nSales by City:")
print(
    df.groupby("City")["Sales"].sum()
)

print("\nAverage Sales by Product:")
print(
    df.groupby("Product")["Sales"].mean()
)

product_sales = (
    df.groupby("Product")["Sales"]
    .sum()
)

print(
    product_sales.idxmax()
)

city_sales = (
    df.groupby("City")["Sales"]
    .sum()
)

print(city_sales.idxmax())

summary = df.groupby("Product").agg({
    "Sales": ["sum", "mean", "max", "min"]
})

print(summary)