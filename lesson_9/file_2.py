print("START FILE_2")

# import file_1 as file_1_alt
# from file_1 import func_from_file_1 as fff_1, a as a_1, b as b_1
from file_1 import *

from sub_dir import CONST_2, CONST_1, get_value, main_func
# import random

def func_from_file_2():
    print(f"Hi form File 2")

# x = random.randint(2, 10)
# y = random.randint(2, 10)

# fff_1(x, y)
# print(f"A from file_1={a_1}")
# print(f"B from file_1={b_1}")
func_from_file_1(2, 2)
print(a)
print(b)
print(some_file_1_value)

result = get_value()

print(CONST_1 * CONST_2)
print(main_func(5))
print(result)
print("END FILE_2")
