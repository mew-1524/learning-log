# Day 32 - Pandas Data Analysis

## Basic Aggregations

sum() → total
mean() → average
max() → maximum
min() → minimum
count() → count values

## Filtering

df[df["Sales"] > 10000]

## Multiple Conditions

& → AND
| → OR
~ → NOT

Example:

df[(df["City"] == "Mumbai") & (df["Sales"] > 5000)]

## Sorting

sort_values()

ascending=True → smallest to largest
ascending=False → largest to smallest

## GroupBy

df.groupby("City")["Sales"].sum()

groupby() → divides data into groups

## Aggregation

agg(["sum", "mean", "max", "min", "count"])

## New Column

df["Revenue"] = df["Sales"] * df["Quantity"]