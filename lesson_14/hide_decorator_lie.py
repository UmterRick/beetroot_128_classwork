import functools
import time


def how_to_call_decorator(expected_type:type=int):
    print(f"Decorator call with {expected_type}")
    def decorator(func):
        print(f"Decorate  {func.__name__}")

        @functools.wraps(func)
        def wrapper(*w_args, **w_kwargs):
            """
            JUST WRAPPER
            :param w_args:
            :param w_kwargs:
            :return:
            """
            print(f"Wrap with {w_args=}, {w_kwargs=}")
            new_args = [expected_type(arg) for arg in w_args]
            result = func(*new_args, **w_kwargs)
            return result

        return wrapper

    return decorator


def measure_time(func, *args):
    print(f"Decorator measure_time get: func={func} {args}")
    @functools.wraps(func)
    def wrapper(*wrapper_args): # та приймає ії аргументи
        print(f"Wrapper measure_time get: {wrapper_args}")
        start_time = time.time()
        func_result = func(*wrapper_args)
        duration = (time.time() - start_time) * 1000
        print(f"Execute {func.__name__} in {duration} ms")
        return func_result
    return wrapper


@how_to_call_decorator(int)
def original_2(a, b):
    """
    Example function for decorator
    :param a:
    :param b:
    :return:
    """
    time.sleep(1)
    print("Original")
    return a + b



r = original_2(1, 2)
print(r)
print()
print(original_2.__doc__)
print(help(original_2))