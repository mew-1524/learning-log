student = {
    "name": "Aadesh",
    "age": 17,
    "city": "Mumbai"
}

print(student.keys())
print(student.values())
print(student.items())

print(student.get("name"))

student.pop("city")

print(student)