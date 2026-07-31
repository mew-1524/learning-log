# Day 018 - OOP Part 3

## Encapsulation

Encapsulation means binding data and methods into a single class while restricting direct access.

Private Variable:

self.__balance

---

## Access Modifiers

Public

self.name

Accessible everywhere.

Protected

self._name

Should only be accessed inside the class and subclasses.

Private

self.__name

Cannot be accessed directly outside the class.

---

## Polymorphism

One interface, many forms.

Example:

Dog.sound()

Cat.sound()

Both have the same method name but different behavior.

---

## Abstraction

Hides implementation details from the user.

Python uses the abc module.

Example:

from abc import ABC, abstractmethod

---

## Advantages

- Better Security
- Data Protection
- Code Reusability
- Easy Maintenance
- Flexible Programs

---

## What I Learned

Today I learned encapsulation, access modifiers, polymorphism, abstraction, and built a banking system.