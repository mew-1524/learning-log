# Day 013 - File Handling

## What is File Handling?

File handling allows us to store and retrieve data from files.

---

## File Modes

"r" → Read

"w" → Write (creates a new file or overwrites existing content)

"a" → Append (adds data at the end)

"x" → Create a new file

---

## Basic Syntax

file = open("sample.txt", "r")

file.read()

file.close()

---

## Better Syntax

with open("sample.txt", "r") as file:
    print(file.read())

---

## Important Methods

read()

Reads the entire file.

write()

Writes data to a file.

close()

Closes the file.

---

## Advantages

- Stores data permanently
- Easy to read and write files
- Used in almost every Python application

---

## What I Learned

Today I learned how to create, read, write, append, and check files in Python.