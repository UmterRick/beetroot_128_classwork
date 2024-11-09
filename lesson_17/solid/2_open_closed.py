from datetime import datetime


class DiscountOld:
    def __init__(self, person, price):
        self.person = person
        self.price = price
        self.values = {
            "user": 0.9,
            "vip": 0.8



        }


    def get_discount(self):
        if self.person == "user":
            return self.price * 0.9

        elif self.person == "VIP":
            return self.price * 0.8

        elif datetime.date().today().isoformat() == "2024.12.31T23:59:59":
            return self.price * 0.5

        elif self.person == "child":
            return self.price * 0.7


############################################


class Discount:
    def __init__(self, price):
        self.price = price

    def get_discount(self):
        return self.price


class UserDiscount(Discount):

    def get_discount(self):
        return self.price * 0.9


class VIPDiscount(Discount):
    def get_discount(self):
        return self.price * 0.85



######################################

class Shape:
    def area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2



class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2


class ShapeAreaCalculator:

    def calculate(self, shape: Shape):
        return shape.area()


