# Day 025 - NumPy Array Manipulation

## concatenate()

Combines arrays.

Example:

np.concatenate((a, b))

---

## vstack()

Stacks arrays vertically.

Example:

np.vstack((a, b))

---

## hstack()

Stacks arrays horizontally.

Example:

np.hstack((a, b))

---

## split()

Splits an array into smaller arrays.

Example:

np.split(array, 2)

---

## Broadcasting

Broadcasting allows NumPy to perform operations
between arrays with compatible shapes.

Example:

array + 5

The value 5 is applied to every element.

---

## Copy

copy() creates an independent array.

Example:

new_array = array.copy()

Changing the copy does not affect the original.

---

## View

view() creates another view of the same data.

Example:

new_array = array.view()

Changing the view can affect the original.

---

## Advanced Indexing

Multiple elements can be selected using indexes.

Example:

array[[0, 2, 4]]

---

## Important Functions

np.concatenate()
np.vstack()
np.hstack()
np.split()
array.copy()
array.view()

---

## What I Learned

Today I learned array manipulation, stacking,
splitting, broadcasting, copy vs view,
and advanced indexing in NumPy.