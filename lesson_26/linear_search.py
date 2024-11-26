import random

from lesson_26.example import timer

@timer
def linear_search(list_a, value):
    for i in range(len(list_a)):
        if list_a[i] == value:
            return i
    return -1


@timer
def linear_search_with_barrier(list_a, value):
    list_a.append(value) # поставити барьер
    i = 0
    while list_a[i] != value:
        i += 1
    # list_a.pop()

    if i == len(list_a):
        return -1
    return i


for i in range(10):
    random_number_list = [random.randint(-500, 500) for _ in range(1000)]
    for j in [10, 56, -100, 342, 212]:
        linear_search(random_number_list, j)
        linear_search_with_barrier(random_number_list, j)
        print("----------------------------------------")

