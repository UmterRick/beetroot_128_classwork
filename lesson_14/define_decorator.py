def decorator(*args):
    print(">>>>", args)
    return 99


def new_logic():
    ...


@decorator  # decorator синтаксичний цукор
def func_1():
    print("I am func 1")
    new_logic()
    return "Hello"


def func_2():
    print("I am func 2")
    new_logic()

    return "Hello"


def func_3():
    print("I am func 3")
    new_logic()

    return "Hello"


new_logic()
r = func_1()


def new_logic_2():
    pass


new_logic_2()
print(r)
