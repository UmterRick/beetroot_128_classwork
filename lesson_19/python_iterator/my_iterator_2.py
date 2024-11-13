x = {
    "a": 1,
    "b": 2,
    "c": 3,
    "d": 4,
    "e": 5,
    "f": 6,
}

class MyDictIterator:
    def __init__(self, data: dict):
        self.data = data
        self.keys = list(data.keys())
        self.counter = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter < len(self.keys):
            key = self.keys[self.counter]
            value = self.data[key]
            self.counter += 1
            return key, value
        raise StopIteration


my_iterator = MyDictIterator(x)
"""
class dict:
    def __iter__(self):
        return self.iterator_class(self) 

"""


for i in my_iterator:
    print(i)
