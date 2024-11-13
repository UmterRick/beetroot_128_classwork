class MyIterator:
    def __init__(self, limit):
        print("CREATE ITERATOR OBJECT")
        self.limit = limit
        self.count = 0

    # def __iter__(self):
    #     print("ASK FOR ITER")
    #     return self

    def __next__(self):
        print("NEXT")
        if self.count < self.limit:
            current = self.count
            # print(f"CALL NEXT with {current=}")
            self.count += 1
            return -current * 2
        raise StopIteration


my_list = list([1, 2, 4, 5, 6])


class MyList(list):

    def __iter__(self):
        self.iterator = MyIterator(len(self))
        return self.iterator

for i in MyList([1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1]):
    # print(i)
    ...