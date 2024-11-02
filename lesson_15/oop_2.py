import datetime


class User: # class - data type
    birthday_date = datetime.date(2000, 1, 1) # class attribute


    def __init__(self, email, name): # method to describe object initialization behaviour -> class constructor
        print("CREATE NEW USER OBJECT", self)
        self.name = name # object attribute
        self.email_address = email # object attribute



user_1 = User("user_1@gmail.com", "USER-1") # __init__()
print(user_1.name, "->", user_1.email_address)
print(user_1.name, "->", user_1.birthday_date)
print("\n\n\n")

user_2 = User("user_2@gmail.com", "USER-2") # __init__()
print(user_2.name, "->", user_2.email_address)
print(user_2.name, "->", user_2.birthday_date)



class Liquid:
    def __init__(self, name):
        self.name = name


    def drink(self):
        ...


def paint():
    ...



