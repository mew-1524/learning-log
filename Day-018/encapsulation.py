class Student:

    def __init__(self, name, marks):
        self.name = name
        self.__marks = marks

    def display(self):
        print("Name :", self.name)
        print("Marks:", self.__marks)

student = Student("Aadesh", 95)

student.display()