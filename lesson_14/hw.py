import functools

def logger(func):
    @functools.wraps(func)
    def wrapper(*args):
        print(f"Function: {func.__name__} with args {args}")
        result = func(*args)
        return result
    return wrapper





@logger

def add(x, y):

    return x + y



@logger

def square_all(*args):

    return [arg ** 2 for arg in args]

square_all(4, 5)
add(4, 5)
