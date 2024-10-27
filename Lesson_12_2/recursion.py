# 0 1 1 2 3 5 8 13 21 34 54
from functools import cache
from pprint import pprint
from random import random


def get_next(a, b):
    return a + b

call_counter = 0
# my_cache = {}

@cache
def fibonacci(n):
    # if n in my_cache:
    #     return my_cache[n]
    global call_counter
    call_counter += 1
    if n <= 0:
        # my_cache[0] = 0
        return 0
    elif n == 1:
        # my_cache[1] = 1
        return 1
    else:
        prev = fibonacci(n-1)
        pre_prev =  fibonacci(n-2)
        # my_cache[n-1] = prev
        # my_cache[n-2] = pre_prev
        return prev + pre_prev



n = 20
for i in range(n):
    print(i, ":", fibonacci(i))
print(f"Calls: {call_counter}")
# pprint(my_cache)



def factorial(n):
    if n <= 1:
        return 1
    factorial_prev = factorial(n-1)
    return n * factorial_prev

x = 6
print(f"Factorial {x}: {factorial(x)}")
result = 1
for i in range(1, x + 1):
    result *= i
print(f"Factorial {x}: {result}")