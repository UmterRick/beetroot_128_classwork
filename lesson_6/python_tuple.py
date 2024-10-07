# tuple
from _ctypes import sizeof

# immutable/mutable - незмінювані/змінювані
some_list = ['a', 'b', 'c']
my_tuple = (0, 1, 2, 4, True, "Hello", ("F", 12, 54), some_list)
my_list = list(my_tuple)

print("4 in tuple:", 4 in my_tuple)
print()
for elem in my_tuple:
    print(elem)


print(my_tuple, id(my_tuple))
print(id(my_tuple[-1]))
my_tuple[-1][2] = "NEW VALUE"

print(my_tuple, id(my_tuple))
print(id(my_tuple[-1]))


# my_tuple_2 = tuple([i for i in range(10_000_000)])
# my_list_2 = list([i for i in range(10_000_000)])
#
# print(my_tuple_2.__sizeof__())
# print(my_list_2.__sizeof__())

# my_tuple[3] = "Third"
# print(my_tuple)
# importtant_info = []
# importtant_info[6] = False


# x = ['a', 'b', 'c', 'd']
#
# a = "hello"
#
# print(id(x))
# x[0] = "e"
# print(x)
# print(id(x))

# x = [i**2 for i in range(0, 10)]
# print(x)



