# polymorphism - poly / morphism
# poly - багато
# morphism - перетворення

class Example:
    def __init__(self, a, b):
        print("Parent Init")
        self.a = a
        self.b = b / 2

    def my_method(self, l, s):
        return l + s


class SubExample(Example):
    def __init__(self, a, b):
        # self.a = a
        # self.b = b
        super().__init__(a, b)

        print("Child INIT")

    def my_method(self, l, s):
        result = super().my_method(l, s)
        return result * 100

sub_obj = SubExample(1, 2)
print(type(sub_obj), sub_obj.a, sub_obj.b)



print(1 + 2)
print(1.5 + 2.9)
print("Hello " + "World")


