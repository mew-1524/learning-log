# Day 024 - NumPy 2D Arrays and Matrix Operations

## 2D Array

A 2D NumPy array contains rows and columns.

Example:

arr = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

---

## Shape

arr.shape

Returns rows and columns.

Example:

(2, 3)

---

## Accessing Elements

arr[row, column]

Example:

arr[0, 1]

---

## Row

arr[1]

---

## Column

arr[:, 0]

---

## Matrix Addition

a + b

---

## Element-wise Multiplication

a * b

---

## Matrix Multiplication

a @ b

or

np.dot(a, b)

---

## Transpose

arr.T

Rows become columns.

Columns become rows.

---

## Axis

axis=0

Performs operation column-wise.

axis=1

Performs operation row-wise.

---

## Important Functions

np.sum()
np.mean()
np.max()
np.min()
np.dot()
arr.T

---

## What I Learned

Today I learned 2D arrays, rows and columns,
matrix operations, transpose, and axis operations
using NumPy.