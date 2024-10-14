def my_func(a, b, c):
    x  = a * b * c
    return  x


def multiply_all(*args):
    print(args, sep="4", end="_")
    print(type(args))
    x = 1
    for i in args:
        x *= i
    return x


def func_with_named_args(arg_1, arg_2, arg_3):
    return arg_1 * arg_2 / arg_3

result = my_func(2, 2, 3)
print(result)

result = multiply_all(1, 2, 4)
print(result)

result = func_with_named_args(arg_2=5, arg_3=3, arg_1=10)
print(result)


def func_with_unlimited_keyword_arguments(**kwargs):
    print(kwargs)
    print(type(kwargs))
    # print(kwargs["name"])

func_with_unlimited_keyword_arguments(x=5, a=10, is_teacher=True)



def some_func(a, b, c, d, *args, **kwargs):
    print(a)
    print(b)
    print(c)
    print(d)
    print(args)
    print(kwargs)


some_func(1, 2, 3,  0, 0, 0, 0, 4, 22, 4, 2, 1, 3, 54, arg_1="Hello", arg_2="World!")

