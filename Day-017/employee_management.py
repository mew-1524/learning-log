class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display(self):
        print("Name   :", self.name)
        print("Salary :", self.salary)

class Developer(Employee):

    def __init__(self, name, salary, language):
        super().__init__(name, salary)
        self.language = language

    def display(self):
        super().display()
        print("Language:", self.language)

name = input("Enter Employee Name: ")
salary = float(input("Enter Salary: "))
language = input("Programming Language: ")

developer = Developer(name, salary, language)

print("\nEmployee Details")
print("-----------------------")
developer.display()