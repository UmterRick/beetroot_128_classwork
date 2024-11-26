import random
import time


def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print(f"{func.__name__} exec in {time.time() - start}")
        return result
    return wrapper

# Для невеликої кількості данних
# + Немає попередніх вимог до данних
# O(n)
@timer
def linear_search(some_list, value):
    for index, element in enumerate(some_list):
        if element == value:
            return index

# Більше підходить для великих данних
# Данні повинні бути відсортовані
# O(log n)
@timer
def binary_search(some_list, value):
    left, right = 0, len(some_list) - 1
    while left <= right:
        mid = (left + right) // 2
        if some_list[mid] == value:
            return mid
        elif some_list[mid] < value:
            left = mid + 1

        elif some_list[mid] > value:
            right = mid - 1
    return None



# Більше підходить рівномірно розподіленими данними
# O (log log n) - average, O(n) - worst case
@timer
def interpolation_search(some_list, value):
    left, right = 0, len(some_list) - 1
    while left <= right and some_list[left] <= value <= some_list[right]:
        mid = left + ((value - some_list[left]) * (right - left)) // (some_list[right] - some_list[left])
        if some_list[mid] == value:
            return mid
        elif some_list[mid] < value:
            left = mid + 1
        else:
            right = mid - 1
    return None


random_number_list = [random.randint(-500, 500) for _ in range(1000)]
sorted_random_number_list = sorted(random_number_list)

print(random_number_list)
print(sorted_random_number_list)

for i in [
    sorted_random_number_list[0],
    sorted_random_number_list[10],
    sorted_random_number_list[99],
    sorted_random_number_list[500],
    sorted_random_number_list[700],
    sorted_random_number_list[999],

]:
    print(f"Search {i}, [{sorted_random_number_list.index(i)}]")
    # linear_search(random_number_list, i)
    x = interpolation_search(sorted_random_number_list, i)
    print(x)
    print()



