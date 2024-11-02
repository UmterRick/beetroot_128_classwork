from functools import cache


class Animal:
    head = 1
    eye = 2
    legs = 4
    sound = "-"
    tail = 1

    def __init__(self, color, name):
        self.color = color
        self.name = name

    def make_sound(self):
        print(f"{self.name} say: {self.sound}")


class Dog(Animal): # Dog - child class; Animal - parent class
    # tail = 1
    sound = "Woof"

    def protect(self):
        print(f"Go away - {self.sound}")


class Horse(Animal):
    # tail = 1
    sound = "brrrr"

    def run_as_a_horse(self):
        print("Run run run")


class Cat(Animal):
    # tail = 1
    sound = "Meow"



my_animal = Animal("gray", "NoName")
my_animal.make_sound()


my_dog = Dog("black", "Jack")
my_dog.make_sound()
my_dog.protect()



class Transport:
    driven_distance = 0


    def __init__(self, color, seats, model, year):
        self.color = color
        self.seats = seats
        self.model = model
        self.year = year


    def ride(self, km):
        self.driven_distance += km



class Cars(Transport):
    wheels = 4
    fuel_per_km = None




class GasCars(Cars):
    fuel = "gas"
    gas_container = 0


    def ride(self, km):
        self.driven_distance += km
        self.gas_container -= self.fuel_per_km



class ElectricCar(Cars):
    battery = 0


    def charge_battery(self, n):
        self.battery += n


    def ride(self, km):
        self.driven_distance += km
        self.battery -= self.fuel_per_km



class Tesla(ElectricCar):
    ...



class TeslaModelX(Tesla):
    ...



class Ship(Transport):
    ...



class Yacht(Ship):
    ...




