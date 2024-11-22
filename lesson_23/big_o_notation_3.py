def sum_big_o(list_1, list_2):
    for i in list_1:
        print(i)

    for j in list_2:
        for k in list_2:
            print(j)


    """
    len(list_1) = 5; len(list_2) = 10 -> 5 + 10 = 15
    n;m -> n + m
    O(n) + O(m) -> O(n+m^2) 
    """


def another_func(list_1, list_2):
    for i in range(min(len(list_1), len(list_2))):
        print(list_1[i], list_2[i])

    """
    O( min(n, m) )
    
    """