class Example:
    CLASS_ATTRIBUTE = 10

    def __init__(self, name, status):
        self.name = name
        self.status = status

    @staticmethod
    def example_method(a, b):
        return a + b


    @classmethod
    def class_attr_formula(cls, x):
        if x > 1:
            cls.example_method(x, 3)
            cls.reg_method(cls("name", "status"), x)
            return cls.CLASS_ATTRIBUTE
        else:
            return 0

    def reg_method(self, x):
        s = self.example_method(x, x ** 2)
        if s / 100 > 1:
            self.status = "READY"


class Geometry:

    @staticmethod
    def sin():
        ...

    @staticmethod
    def cos():
        ...

    @staticmethod
    def tan():
        ...


Geometry.sin()

Geometry.cos()

print(Example.example_method(2, 2))
print(Example.class_attr_formula(-5))

