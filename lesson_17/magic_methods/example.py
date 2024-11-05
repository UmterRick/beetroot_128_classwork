# magic method - dunder method - double underscored method
from math import sqrt


class Example:

    def __init__(self, x):
        print("I am __init__")
        self.x = x

    def __str__(self):
        return f"Example(x={self.x} Dunder method )"

    # def __repr__(self):
    #     ...

    def init(self, x):
        print("I am init")
        return x


class MyInt:
    def __init__(self, value):
        self.value = value


    def __eq__(self, other):
        return self.value==other.value


    # def __gt__(self, other):


    # def __ge__(self, other):
# obj = Example(3)

# print(obj)
# obj.init(5)

print(9 ** 0.5)


class Car:
    def __init__(self, power):
        self.power = power




    def __add__(self, other):
        raise Exception("You are in car accident")

    def __sub__(self, other):
        if isinstance(other, Car):
            new_power = self.power - other.power
            return Car(new_power)

        if isinstance(other, Wheel):
            print("You have a motorcycle now")


    def __str__(self):
        return f"Car({self.power})"




class Wheel:
    ...




x = Car(1000)

y = Car(800)
w = Wheel()
print(x - y)
