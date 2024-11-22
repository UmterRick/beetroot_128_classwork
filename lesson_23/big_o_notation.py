"""
O(1)
O(n)

"""

def constant_time(some_list): # O(1)
    ### adr[x] = adr[0] + obj_size * x
    return some_list[5]


def linear_time(some_list): # O(n)
    for i in some_list:
        print(i)

    """
    len(some_list) = 10 -> actions = 10
    len(some_list) = 100 -> actions = 100
    """

def quadratic_time(some_list): # O(n^2)
    for i in some_list:
        for j in some_list:
            print(i, j)

    """
    len(some_list) = 10 -> actions = 10 * 10 = 100 -> 10^2
    len(some_list) = 100 -> actions = 100 * 100 = 10_000 -> 100^2
    """




