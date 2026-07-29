class Student:

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def show(self):
        print(self.name, "-", self.marks)

student1 = Student("Aadesh", 92)
student2 = Student("Rahul", 85)
student3 = Student("Riya", 96)

student1.show()
student2.show()
student3.show()