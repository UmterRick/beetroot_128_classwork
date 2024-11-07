import datetime

class ExploreMagicMethods:
    # __package__ = "beetroot"
    def __init__(self, values):
        self.values = values

    def __len__(self):
        print("Get LEN for OBJ")
        return len(self.values)

    def __format__(self, format_spec):
        return format_spec.join(str(value) for value in self.values)


    def __del__(self):
        print("Goodbye python!")


obj = ExploreMagicMethods([1, 2, 3, 4, 5])
print(obj)
x = format(obj, ", ")
print(x)


today = datetime.datetime.today()
print(today)


print(today.strftime("%d (%A) %B %Y"))
s = f"Now is "
print(s)
