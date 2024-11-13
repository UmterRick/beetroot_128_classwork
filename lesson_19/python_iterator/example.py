# list_1 = [1, 2, 3, 4, 5, 6]
#
# for i in list_1:
#     print(i)
#
# for i in tuple(list_1):
#     print(i)
#
# for i in {"a": 1, "b":2, "c": 3, "d":4}:
#     print(i)


class IteratorExample:
    def __init__(self):
        ...

    def __iter__(self):
        ...

    def __next__(self):
        ...

y = list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12 ,12])

for i in y:
    print(i)

#
# y_iterator = y.__iter__()
# i = next(y_iterator)
# print(i)
# i = next(y_iterator)
# print(i)
# i = next(y_iterator)
# print(i)
# i = next(y_iterator)
# print(i)
# i = next(y_iterator)
# print(i)

class MyList:

    def __iter__(self):
        return self.iterator()

print("----" * 20)
y_iterator_2 = y.__iter__()
while True:
    try:
        i = next(y_iterator_2)
        ###
        print(i)
        print(y)
        ###
    except StopIteration:
        break