print("List Comprehension")
my_list_1 = []
for i in range(100):
    my_list_1.append(i/10)
print(my_list_1)

my_list_2 = [ i/10 for i in range(100) ]
print(my_list_2)

print()
print("Dict Comprehension")
my_dict_1 = {}
for i in range(100):
    my_dict_1[f"key_{i}"] = i / 10
print(my_dict_1)


my_dict_2 = {f"key_{i}": i / 10 for i in range(100)}
print(my_dict_2)


