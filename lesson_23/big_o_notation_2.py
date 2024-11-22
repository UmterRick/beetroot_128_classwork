def binary_search(some_list, value):  # O(log n)
    left, right = 0, len(some_list) - 1
    while left <= right:
        mid = (left + right) // 2
        if some_list[mid] == value:
            return mid

        elif some_list[mid] < value:
            left = mid + 1

        else:
            right = mid - 1
    return False


# [1, 2, 3, 4, 5, 7, 9, 12, 15, 22, 34, 35]

"""
O(2n) - linear -> O(n) 
O(3n) - linear -> O(n)
"""


def guess_big_O(list_a, list_b, list_c):
    list_a = list_a + list_a
    for i in list_a: # 5
        for j in list_b: # 10
            binary_search(list_c, j)

    """
    len(list_a) = 5; len(list_b) = 10 -> actions = 5 * 10 = 50
    len(list_a) = 10; len(list_b) = 20 -> actions = 10 * 20 = 200
    """

    """
    O(n) * O(n) -> O(n^2)
    O(2n) * O(m) * O(log k) -> O(n * m * log k)
    """

def fibonacci(n): # O(2^n)

    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


fibonacci(10)

