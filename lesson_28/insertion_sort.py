def insertion_sort_clear(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def insertion_sort(arr): # worst: O(n^2), best O(n), average O(n^2)
    print(f"Original data: {arr}\n")
    for i in range(1, len(arr)):
        print(f"Iteration {i}")
        key = arr[i]
        print(f"Key  = {arr[i]}")
        j = i - 1
        print(f"Start with j={j}")
        while j >= 0 and arr[j] > key:
            print(f"Is {j} >= 0 and {arr[j]} > {key}? -> YES")
            print(arr)

            arr[j + 1] = arr[j]
            j -= 1

            print(arr)
            print(f"Set that right index for {key} is {j+1}")
            print()

        arr[j + 1] = key

        print("After:", arr)
        print("--------------" * 10, "\n")
    return arr


x = [50, 30, 64, 12, 100, 21, 45 ]
# [1, 6, 2, 7, 3, 4, 5]
# [1, 2, 6, 7, 3, 4, 5]
# [1, 2, 3, 7, 6, 4, 5]
print(x)
insertion_sort(x)
print(x)
