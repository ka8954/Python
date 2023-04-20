class Vehicle:

    def tollfee(self):
        print("\nPAY TOLL FEE")

class Car(Vehicle):

    def __init__(self):
        self.name = "THAR"
        self.tyres = 4
        self.fueltype = "Petrol"
        self.capacity = 6

    def showdet(self):
        print("\nName : ", self.name)
        print("No of Wheels : ", self.tyres)
        print("Fuel Type : ", self.fueltype)
        print("Capacity : ", self.capacity)

class Bike(Vehicle):

    def __init__(self):
        self.name = "RE"
        self.tyres = 2
        self.fueltype = "Petrol"
        self.capacity = 2

    def showdat(self):
        print("\nName : ", self.name)
        print("No of Wheels : ", self.tyres)
        print("Fuel Type : ", self.fueltype)
        print("Capacity : ", self.capacity)

c1 = Car()
c1.showdet()
c1.tollfee()

b1 = Bike()
b1.showdat()
b1.tollfee()
