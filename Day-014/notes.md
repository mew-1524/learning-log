# Day 014 - Exception Handling

## What is an Exception?

An exception is an error that occurs while a program is running.

Examples:

- Division by zero
- Invalid input
- File not found

---

## try

Code that may cause an error is written inside the try block.

Example:

try:
    print(10 / 0)

---

## except

Handles the error.

Example:

except ZeroDivisionError:
    print("Cannot divide by zero.")

---

## else

Runs only if no exception occurs.

---

## finally

Always executes whether an exception occurs or not.

---

## raise

Used to create your own exception.

Example:

raise Exception("Invalid Age")

---

## Advantages

- Prevents program crashes
- Makes programs user-friendly
- Easier debugging
- Handles unexpected errors

---

## What I Learned

Today I learned how to use try, except, else, finally, and raise to handle errors in Python.