def selection_sort(arr): # always O(n^2)
    n = len(arr)
    for i in range(n):
        index_min_element = i
        print(f"Iteration {i + 1}")
        print("Before:", arr)
        print(f"Min element goes to {i} index")
        print(f"\nSearch for min element from {arr[i + 1:]}")
        for j in range(i + 1, n):
            print(f"\t Is {arr[j]} < {arr[index_min_element]}?")
            if arr[j] < arr[index_min_element]:
                print(f"\t\t YES: Min element now on index {j} -> {arr[j]}")
                index_min_element = j
            else:
                print(f"\t\t No: Skip")

        print(f"Swap elements idx({i}) and  idx({index_min_element}) -> swap {arr[index_min_element]} <-> {arr[i]}")
        arr[i], arr[index_min_element] = arr[index_min_element], arr[i]
        print()
        print("After:", arr)
        print("----------" * 10, "\n")
    return arr


x = [6, 1, 7, 3, 3, 3, 4, 2, 5, 2]
# [1, 6, 2, 7, 3, 4, 5]
# [1, 2, 6, 7, 3, 4, 5]
# [1, 2, 3, 7, 6, 4, 5]
print(x)
selection_sort(x)
print(x)
