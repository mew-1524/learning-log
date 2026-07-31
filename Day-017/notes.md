# Day 017 - OOP Part 2 (Inheritance)

## What is Inheritance?

Inheritance allows one class to acquire the properties and methods of another class.

---

## Types of Inheritance

1. Single Inheritance

One child inherits one parent.

2. Multilevel Inheritance

Grandparent → Parent → Child

3. Hierarchical Inheritance

One parent has multiple child classes.

(Multiple inheritance is also supported in Python.)

---

## Method Overriding

A child class can redefine a method from the parent class.

Example:

class Animal:
    def sound(self):
        print("Animal")

class Dog(Animal):
    def sound(self):
        print("Dog")

---

## super()

super() is used to call the parent class constructor or methods.

Example:

super().__init__(name)

---

## Advantages

- Code Reusability
- Less Code Duplication
- Better Organization
- Easy Maintenance

---

## What I Learned

Today I learned inheritance, method overriding, and the super() function in Python.