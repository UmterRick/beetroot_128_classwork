# Bubble Sort
import random
import time


def bubble_sort(arr):  # worst: O(n^2), best O(n), average O(n^2)
    data = arr.copy()
    n = len(data)
    # print(f"Sort array with {n} elements")
    # for(i=0, i<n, i++)
    for i in range(n - 1):
        # print(f"{i+1} Iteration:")
        # print(f"Look for elements form 0 to {n-i-1}")
        for j in range(n - i - 1):
            # print(f"Data: {data}, J = {j}")
            # print(f"Is {data[j]} > {data[j+1]}")
            if data[j] > data[j + 1]:
                # print(f"YES: swap {data[j]} and  {data[j + 1]}")
                temp = data[j + 1]

                data[j + 1] = data[j]
                data[j] = temp
                # print(data)
            # else:
            # print("No -> Skip")
            # print("------" * 10)
            # print()
    return data


# [4, 5, 3, 2, 7, 1]: 5 <-> 3
# [4, 3, 5, 2, 7, 1]
# x = [6, 4, 5, 3, 2, 7, 1]
x = [6, 1, 7, 3, 3, 3, 4, 2, 5, 2]
#  [1, 2, 6, 7, 3, 4, 5, ]
# test_list = [random.randint(-1000, 1000) for i in range(0, 100_000)]

print("Start")
start_time = time.time()

sorted_x = bubble_sort(x)
print(time.time() - start_time)
print(x)

print(sorted_x)
