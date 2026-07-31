class Vehicle:

    def start(self):
        print("Vehicle Started")

class Car(Vehicle):

    def drive(self):
        print("Car is Driving")

class Bike(Vehicle):

    def ride(self):
        print("Bike is Riding")

car = Car()
bike = Bike()

car.start()
car.drive()

bike.start()
bike.ride()