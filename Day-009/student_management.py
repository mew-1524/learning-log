students = {
    "Aadesh": 91,
    "Rahul": 84,
    "Riya": 95,
    "Aman": 88
}

print("Student Marks")

for name, marks in students.items():
    print(name, ":", marks)

highest = max(students, key=students.get)

print("\nTopper:", highest)
print("Marks:", students[highest])