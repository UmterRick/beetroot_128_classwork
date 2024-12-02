def merge_sort(arr): #Time complexity: O(n*log n), Memory complexity: O(n)
    if len(arr) <= 1:
        print(f"{arr} not possible to sort return back")
        return arr

    mid_idx = len(arr) // 2
    left_arr = arr[:mid_idx]
    right_arr = arr[mid_idx:]
    print(f"Split {arr} into {left_arr} and {right_arr}")

    left_arr = merge_sort(left_arr)
    right_arr = merge_sort(right_arr)
    print()
    return merge(left_arr, right_arr)





# [9, 7, 2, 1]
# L: [9, 7] R: [2, 1]
# S_L [7, 9] S_R: [1, 2]
# [7, 9, 1, 2] wrong result
# [1, 2, 7, 9] right result




def merge(left_part, right_part):
    res = []
    print(f"========= {left_part} < MAGIC MERGE > {right_part} ==========")
    while len(left_part) != 0 and len(right_part) != 0:
        print("\tCompare first elements (min for each part)")
        print(f"\tIS {left_part[0]} < {right_part[0]}")
        if left_part[0] < right_part[0]:
            res.append(left_part[0])
            print(f"\tYES: {res=}")
            left_part.remove(left_part[0])
        else:
            res.append(right_part[0])
            print(f"\tNO: {res=}")
            right_part.remove(right_part[0])

        print(f"\tLeft Part: {left_part}")
        print(f"\tRight Part: {right_part}")
        print()

    print(f"\tLeft part after removing: {left_part}")
    print(f"\tRight part after removing: {right_part}")
    if len(left_part) == 0:
        print(f"\tAdd {res} + {right_part}")
        res = res + right_part
    else:
        print(f"\tAdd {res} + {left_part}")
        res = res + left_part
    # print(res)
    return res

x = [50, 64, 30, 12, 100, 21, 45 ]
print(x)
y = merge_sort(x)
print(y)
