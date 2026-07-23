# Day 011 - Functions in Python

## What is a Function?

A function is a block of reusable code that performs a specific task.

Example:

def greet():
    print("Hello")

greet()

---

## Advantages

- Reuse code
- Reduce repetition
- Easy to understand
- Easy to maintain

---

## Syntax

def function_name():
    statements

function_name()

---

## Parameters

Values written in the function definition.

Example:

def greet(name):
    print(name)

---

## Arguments

Values passed while calling the function.

Example:

greet("Aadesh")

---

## Return Statement

The return keyword sends a value back.

Example:

def add(a, b):
    return a + b

---

## Default Argument

def student(name, city="Mumbai"):
    print(name, city)

---

## Keyword Argument

student(city="Pune", name="Rahul")

---

## What I Learned

Today I learned how to define functions, pass parameters, use return values, and work with default and keyword arguments.