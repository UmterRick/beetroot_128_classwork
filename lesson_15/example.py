import json

from lesson_3.numbers import value


class Coordinates:
    def __init__(self, x, y):
        self.validate_axis(x)
        self.validate_axis(y)
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Coordinate(x={self.x}, y={self.y})"

    def validate_axis(self, n):
        if not isinstance(n, int) and not isinstance(n, float):
            raise TypeError("Axis values can by only int of float")

    def add(self, coord):
        if not isinstance(coord, Coordinates):
            raise TypeError(f"Cant add Coordinates to {type(coord)}")

        new_x = self.x + coord.x
        new_y = self.y + coord.y
        return Coordinates(new_x, new_y)


point_0 = (1, 1)
point_1 = Coordinates(2, 1)
point_2 = Coordinates(5, 3)

point_3 = point_1.add(point_2)
print(point_3)


def print_hello():
    print("Hello")


class MyClass:
    def __init__(self):
        print_hello()


x = MyClass()


class Address:
    def __init__(self, country, city, street):
        self.country = country
        self.city = city
        self.street = street

    def validate(self):
        return

    def show_as_dict(self):
        return {
            "country": self.country,
            "city": self.city,
            "street": self.street,
        }


class Contact:
    def __init__(self, number, name, surname, address: Address):
        self.validate()
        self.number = number
        self.name = name
        self.surname = surname
        self.address = address

    def validate(self):
        return

    def show_as_dict(self):
        return {
            self.number: {
                "name": self.name,
                "address": self.address.show_as_dict()
            }

        }


class Phonebook:
    def __init__(self, file_name: str):
        self.file_name = file_name
        self.file = None
        self.contacts: list[Contact] = self.get_contacts()

    def add_contact(self, new_contact: Contact):
        self.contacts.append(new_contact)

    def get_contacts(self):
        with open(self.file_name) as file:
            d = json.load(file)
            ...
        return d

    def save_contacts(self):
        contacts = {}
        for contact in self.contacts:
            contact_dict = contact.show_as_dict()
            contacts.update(contact_dict)


        with open(self.file_name) as file:
            json.dump(contacts, file)


book = Phonebook("my_file.json")