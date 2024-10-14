from lesson_6.python_tuple import my_tuple


def is_positive(a):
    print("Start function")
    if a > 0:
        print("Is positive")
        return True
    else:
        print("Is negative")
        return False

def is_positive_2(a):
    print("Start function")
    if a > 0:
        print("Is positive")
        result = True
    else:
        print("Is negative")
        result = False
    return result

x = is_positive(-5)
print(x)

# result = return_experiment()
# print("\nResult:", result)


def get_user_name():
    return input("Name:").split(" ")

# name, last_name = get_user_name()

# print("Your name is: ", name)
# print("Your last name is: ", last_name)


def rectangle_area(a, b):
    area = a * b
    return area

def car_fabric(wheels, seats, engine, color):
    print(f"install engine: {engine} ")
    print(f"fix seats : {seats}")
    print(f"attach wheels {wheels} x4")
    print(f"paint case: {color}")
    return f"{color} Car with {engine} and 4 {wheels}"


my_car = car_fabric("Hancock", "leather", "V8", "Black")
print(my_car)
print("\n\n\n")
x = 10
y = 20
my_area = rectangle_area(x, y)
print(my_area)