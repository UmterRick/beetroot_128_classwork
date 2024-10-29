# set - множина

my_set = {1, 2, 3, 4, 1, 1, 3, 2, 5, 3, 3, 4}
my_list = [1, 2, 3, 4, 1, 1, 3, 2, 5, 3, 3, 4]
my_tuple = (1, 2, 3, 4, 1, 1, 3, 2, 5, 3, 3, 4)
print(" list: ", my_list)
print("tuple: ", my_tuple)
print("  set: ", my_set)


new_set = {1, 2, 22, 2, 2, 2, 3, "Hello", "Hello", (12, 12, 13), (12, 12, 13)}
print(new_set)
# print(new_set["Hello"]) unable
# for i in range(10):
#     print(new_set)

# Warning !
# x_1 = new_set.pop()
# x_2 = new_set.pop()
# x_3 = new_set.pop()
# x_4 = new_set.pop()
# print(x_4)

a_dict = {"a": 1, "b": 2}
if "c" in a_dict:
    print(a_dict["c"])

if "Hello" in new_set:
    print("Removing 'Hello' element ...")
    new_set.remove("Hello")
print(new_set)

new_set.update({4, 5, 6, 7, 1, 2, 3, 1})
print(new_set)

new_set.add(456)
print(new_set)


