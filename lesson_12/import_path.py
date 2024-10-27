import sys

for i in sys.path:
    print(i)
sys.path.clear()
print("-------------------------------")
print(sys.path)

import some_package
print(some_package.useful_func_6())



