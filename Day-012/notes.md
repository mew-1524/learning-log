# Day 012 - Lambda, map(), filter(), Recursion

## Lambda Function

A lambda function is a small anonymous function.

Syntax:

lambda arguments: expression

Example:

square = lambda x: x * x

---

## map()

Applies a function to every element.

Example:

map(lambda x: x * x, numbers)

---

## filter()

Filters elements based on a condition.

Example:

filter(lambda x: x % 2 == 0, numbers)

---

## Recursion

A function calling itself.

Example:

def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)

---

## Advantages

- Short code
- Cleaner programs
- Useful in Data Science
- Powerful for solving mathematical problems

---

## What I Learned

Today I learned lambda functions, map(), filter(), recursion, and created a mini number utility project.