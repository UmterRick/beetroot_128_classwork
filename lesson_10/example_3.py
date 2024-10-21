import random

try:
    print("Connect")
    x = random.randint(0, 10)
    print(f"x = {x}")
    print([1, 2, 3, 4][x])
    try:
        raise ValueError

    except ValueError:
        raise TypeError


except IndexError:
    print("Not existing index")

except TypeError:
    ...
else:
    print("All is good -> No errors")
finally:
    print("Finally -> close connection")


