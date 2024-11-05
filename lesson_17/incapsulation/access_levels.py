import random


class ExampleClass:
    """
    name - public
    _name - protected
    __name - private
    """

    __class_attribute = 1  # private

    def __init__(self, name):
        self._instance_attribute = 2  # protected
        self.name = name # public
        self.new_attr = self._protected_method(self._instance_attribute)

    def public_method(self, arg_1, arg_2):  # public
        x = self.__private_method(self.__class_attribute)
        return arg_2 * arg_1 / x

    def __integral_func_1(self):
        ...

    def __integral_func_2(self):
        ...


    def get_math_result(self, x):
        x_1 = self.__integral_func_1()
        x_2 = self.__integral_func_2()
        result = min((x_1, x_2))
    def _protected_method(self, arg_1):
        return arg_1 + 100

    def __private_method(self, a):
        return a * a


# Repeat oop intro
# x = ExampleClass
# print(x)
# print(x.class_attribute)
# obj_x = ExampleClass("Name 1")
# obj_y = x("Name 2")
# print(obj_x.example_method(12, 3))
# print(obj_y.example_method(12, 3))
# print(x.example_method(obj_x, 10, 20))

example_object = ExampleClass("Example")
print(example_object.name)
print(example_object.new_attr)
print(example_object.public_method(2, 4))
print(example_object._protected_method(123))
print(example_object.__private_method(5))



"""
public - have access from anywhere

protected - better not use or modify from outer code 

private - access only from class itself 

"""


class Item:

    def __init__(self, name, price):
        self.__id = self.__generate_unique_id()
        self.name = name
        self.price = price


    def __generate_unique_id(self):
        return "".join([str(random.randint(0, 9)) for i in range(10)])

    def save_to_db(self):
        ...




item_1 = Item("Tomato", 100)
item_1.__id = "djsandaskjdnassakdasn"
item_1.save_to_db()




