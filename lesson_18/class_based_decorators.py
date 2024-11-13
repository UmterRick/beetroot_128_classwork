import functools
import time
import datetime


# def in_seconds(func):
#     @functools.wraps(func)
#     def wrapper(*args, **kwargs):
#         start_time = time.time()
#         result = func(*args, **kwargs)
#         d = time.time() - start_time
#         print(f"Function {func.__name__} was exec in {d} s")
#         return result
#
#     return wrapper
#
#
# def in_milliseconds(func):
#     @functools.wraps(func)
#     def wrapper(*args, **kwargs):
#         start_time = time.time()
#         result = func(*args, **kwargs)
#         d = (time.time() - start_time) * 1000
#         print(f"Function {func.__name__} was exec in {d} ms")
#         return result
#
#     return wrapper


class Timer:
    def __init__(self, dt_fmt):
        self.format = dt_fmt



    def __print_from_to(self, start_time):
        end_time = time.time()
        print(f"Function executed from {datetime.datetime.fromtimestamp(start_time).strftime(self.format)} to {datetime.datetime.fromtimestamp(end_time)}")

    def in_seconds(self, func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            start_time = time.time()
            result = func(*args, **kwargs)
            d = time.time() - start_time
            print(f"Function {func.__name__} was exec in {d} s")
            self.__print_from_to(start_time)
            return result

        return wrapper

    def in_milliseconds(self, func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            start_time = time.time()
            result = func(*args, **kwargs)
            d = (time.time() - start_time) * 1000
            print(f"Function {func.__name__} was exec in {d} ms")
            self.__print_from_to(start_time)
            return result

        return wrapper



@Timer("%M:%S").in_seconds
def example_func(a, b, c):
    print("FUNC SLEEP")
    time.sleep(a)
    print("FUNC AWAKE")
    return b - c


example_func(1, 3, 1)
