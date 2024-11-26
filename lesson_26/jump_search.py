import math
import random


def jump_search(list_a, value):
    length = len(list_a)

    jump = int(math.sqrt(length)) # розмір стрибка за яким ми будем ссуватись по оригінальному списку
    left_index, right_index = 0, 0 # індекс крайніх елементів на поточномо проміжку оригінального списку який ми розглядаемо

    # Поки лівий край не вийшов за край оригінального списку ТА значення лівого краю меньше ніж ціль
    while left_index < length and list_a[left_index] <= value:

        # Права частина зрізу це лівий край + стрибок ( lenght = 102, jump = 10, left=100, right=min(102, 110) )
        right_index = min(length - 1, left_index + jump)

        # Якщо Ціль між лівим і правим краемб зупинити стрибки по оригінальному списку
        if list_a[left_index] <= value and list_a[right_index] >= value:
            break

        #  Якщо Цілі в цьому проміжку немає -> Стрибай
        left_index += jump


    # Якщо дострибався так що лівий край вийшов за межі оригінального списку або лівий край вже більше цілі, то Цілі тут не знайти
    if left_index >= length or list_a[left_index] > value:
        return -1

    right_index = min(length - 1, right_index)
    i = left_index

    while i <= right_index and list_a[i] <= value:
        if list_a[i] == value:
            return i
        i += 1
    return -1


random_number_list = sorted([random.randint(-500, 500) for _ in range(1000)])
search_for = random_number_list[ random.randint(0, 999)]
x = jump_search(random_number_list, search_for)
print(x)