class Animal:

    def eat(self):
        print("Animal is eating.")

class Dog(Animal):

    def bark(self):
        print("Dog is barking.")

class Puppy(Dog):

    def weep(self):
        print("Puppy is weeping.")

puppy = Puppy()

puppy.eat()
puppy.bark()
puppy.weep()