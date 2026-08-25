# Day 027 - Pandas Basics

## What is Pandas?

Pandas is a Python library used for data manipulation
and data analysis.

It is commonly used for working with structured data
such as CSV files and tables.

---

## Import Pandas

import pandas as pd

---

## Series

A Series is a one-dimensional labeled data structure.

Example:

pd.Series([10, 20, 30])

---

## DataFrame

A DataFrame is a two-dimensional data structure
containing rows and columns.

Example:

pd.DataFrame(data)

---

## Series vs DataFrame

Series:
1D
Usually represents one column.

DataFrame:
2D
Contains rows and columns.

---

## Important DataFrame Properties

df.shape
df.columns
df.index
df.dtypes

---

## Selecting Columns

df["Name"]

Multiple columns:

df[["Name", "Marks"]]

---

## Selecting Rows

iloc -> integer position

df.iloc[0]

loc -> label

df.loc["S1"]

---

## DataFrame Statistics

df["Marks"].mean()
df["Marks"].max()
df["Marks"].min()
df["Marks"].sum()

---

## Filtering

df[df["Marks"] > 80]

---

## Adding Columns

df["Result"] = "Pass"

---

## Reading CSV

df = pd.read_csv("students.csv")

---

## First and Last Rows

df.head()
df.tail()

---

## idxmax()

Returns the index of the maximum value.

df["Marks"].idxmax()

---

## What I Learned

Today I learned the basics of Pandas,
including Series, DataFrames, indexing,
filtering, statistics, calculated columns,
and reading CSV files.