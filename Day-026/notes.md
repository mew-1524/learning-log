# Day 026 - NumPy Revision and Student Performance Analysis

## NumPy Revision

NumPy is a Python library used for numerical and
array-based computations.

## Important Properties

shape
size
ndim

## Important Functions

np.sum()
np.mean()
np.max()
np.min()
np.std()

## Indexing

array[index]

## Slicing

array[start:end]

## Boolean Filtering

array[array > value]

Example:

marks[marks >= 80]

## 2D Arrays

A 2D array contains rows and columns.

Example:

array = np.array([
    [10, 20],
    [30, 40]
])

## Axis

axis=0 -> column-wise operation

axis=1 -> row-wise operation

## Broadcasting

Allows operations between arrays with compatible shapes.

Example:

marks + 5

adds 5 to every element.

## Copy

array.copy()

Creates an independent copy.

## View

array.view()

Creates a view that can share the same underlying data.

## Today's Project

Built a Student Performance Analysis using NumPy.

The project calculates:

- Overall average
- Highest mark
- Lowest mark
- Student-wise average
- Subject-wise average
- Top students
- Bonus marks
- Filtered marks

## What I Learned

Today I revised NumPy and applied array operations
to a practical student performance analysis project.