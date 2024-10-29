from typing import Callable

def func_1():
    print("I am func 1")
    return 1


def func_2():
    print("I am func 2")
    return 2


def some_func(f_a: Callable, f_b: Callable, call_a: bool = True, *args, **kwargs):
    if call_a:
        result = f_a(*args)
    else:
        result = f_b(**kwargs)
    return result



def example_func(a, b):
    return a + b
#func_1() # type=int value=1

print(">", func_1) # function object
print(120)
print(">", func_1()) # function call


age = 10
years = 5
example_func(age, years)

print("----" * 10)
def func_3(prefix, suffix):
    return prefix +  " Hello World " + suffix

res = some_func(func_3, func_1, True, "START", "END")

print(f"Some func result = {res}")



def call_with_all_strings(func: Callable, *args):
    args = [str(arg) for arg in args]
    result = func(args)
    return result

res = call_with_all_strings(" - ".join, 1, 2, 3, 4, 5, 6, 7, 8)
print(res)

def flip_number(n):
    return -n

def make_percent(n):
    return n / 100

result_a = flip_number(10)
print(result_a)


def transform_number(number, action_1, action_2):
    if  0 < number < 100:
        r = action_1(number)
        # r = float(89)
    else:
        r = action_2(number)
        # r = str(999)
    return r

def make_type(obj, expected_type):
    if isinstance(obj, str):
        if obj.isdigit():
            ...
    try:
        return expected_type(obj)
    except:
        ...

transform_number(89, make_percent, flip_number)
transform_number(89, flip_number, make_percent)
transform_number(89, float, str)



print(make_type(3, str))
print(make_type("111", float))
