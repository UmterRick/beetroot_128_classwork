from statistics import mean

my_list = [0, 1, 3, 12, "HGello"]
print(my_list)

my_list.append(True)
print(my_list)

my_list += [12, 4, 5,  6, 7]
print(my_list)
print(len(my_list))

# my_list.clear()
# print(my_list)

my_list.reverse()
print(my_list)

my_list.insert(-2, "Inserted_element")
print(my_list)

x = my_list.pop()
print(my_list)
print(x)


x = my_list.pop(5)
print(my_list)
print(x)


my_list.extend([1, 2, 34, 4, 5])
print(my_list)
my_list.extend("TEXT")
print(my_list)


find_index = my_list.index(5)
print(find_index)

find_index = my_list.index(5, 4)
print(find_index)

my_list.insert(3, 5)
my_list.insert(10, 5)
my_list.insert(8, 5)

search_for = 5
start = 0
search_element_amount = my_list.count(search_for)
print(f"We know that there are {search_element_amount}  '{search_for}' in list")
for i in range(0, search_element_amount):
    index = my_list.index(5, start)
    print(f"We found {search_for} at index {index}")
    start = index + 1

print("\n\n")
my_list.remove(12)
print(my_list)


print(my_list)


some_list = {3, 5, 1, 5, 34, -3, 12, 5}
print(mean(some_list))
print(min(some_list))
