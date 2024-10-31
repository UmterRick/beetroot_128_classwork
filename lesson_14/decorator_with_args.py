def how_to_call_decorator(expected_type:type=int):
    print(f"Decorator call with {expected_type}")
    def decorator(func):
        print(f"Decorate  {func.__name__}")
        def wrapper(*w_args, **w_kwargs):
            print(f"Wrap with {w_args=}, {w_kwargs=}")
            new_args = [expected_type(arg) for arg in w_args]
            result = func(*new_args, **w_kwargs)
            return result

        return wrapper

    return decorator


# @how_to_call_decorator(bool)
def function(a, b):
    return a + b

@how_to_call_decorator
def func_2(a, b):
    return a - b

print(function(10, 20))


new_function = how_to_call_decorator(int)(function)

print(new_function)

new_function(10, 20)





