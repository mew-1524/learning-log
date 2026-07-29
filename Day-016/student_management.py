class Student:

    def __init__(self, name, roll, marks):
        self.name = name
        self.roll = roll
        self.marks = marks

    def display(self):
        print("\nStudent Details")
        print("----------------")
        print("Name :", self.name)
        print("Roll :", self.roll)
        print("Marks:", self.marks)

name = input("Enter Student Name: ")
roll = input("Enter Roll Number: ")
marks = float(input("Enter Marks: "))

student = Student(name, roll, marks)

student.display()