import datetime
import math


class User:
    def __init__(self, email, birth_date: datetime.date):
        self.__email = email
        self.__name = "John Doe"
        self.birth_date = birth_date

    @property  # getter
    def username(self):
        print("\n >>> Get private __name")
        return self.__name


    @username.setter  # setter
    def username(self, new_name):
        if not isinstance(new_name, str):
            raise TypeError
        self.__name = new_name

    @username.deleter
    def username(self):
        self.__name = self.__email

    @property
    def email(self):
        print("\n >>> Get private __email")
        mail, domen = self.__email.split("@")


        return "*"*len(mail)+"@"+domen

    @property
    def age(self):
        x =  datetime.date.today() - self.birth_date
        return x.days // 365





my_user = User("my_email@mail.com", datetime.date(2000, 1, 1))
print(my_user.email)

print(my_user.username)
my_user.username = "New User Name"
print(my_user.username)
del my_user.username
print(my_user.username)

print("#################")
print(my_user.age)
print(my_user.birth_date)



class Circle:
    def __init__(self, radius):
        self.radius = radius

    @property
    def area(self):
        return math.pi * (self.radius ** 2)


x = Circle(3)

print(x.area)


class Percent:
    def __init__(self, value):
        self.__value = self.__validate_and_transform(value)

    @staticmethod
    def __validate_and_transform(value):
        if  0 <= value <= 100 and not isinstance(value, float):
            return value

        elif 0 <= value <=1:
            return value * 100

        raise ValueError("Wrong Percent value")

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, new_value):
        self.__value = self.__validate_and_transform(new_value)



    def __str__(self):
        return f"{self.__value} %"


discount = Percent(34)


print(discount)
discount.value = 20
print(discount)
# discount.value = 200

print(discount.value)

