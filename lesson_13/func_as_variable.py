def func_1():
    print("I am func 1")
    return 1


def func_2():
    print("I am func 2")
    return 2

# a = func_1
#
# print(func_1)
# print(func_1())
# print()
# print(a)
# print(a())

l = [func_1, func_2]
for i in l:
    x = i()
    print(x)


def subtract(values):
    return sum([-i for i in values])


d = {
    "+": sum,
    "-": subtract
}

operator = input("Action: ")
values = input("Values: ")
clear_values = []
for i in values.split(","):
    clear_values.append(int(i.strip()))

math_operation = d.get(operator)
if math_operation is not None:
    result = math_operation(clear_values)
    print(result)