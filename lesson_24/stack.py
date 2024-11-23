"""
Stack - Last In First Out (LIFO)

Hello

o
l
l
e
h

olleh
"""


class Stack:
    def __init__(self):
        self.__items = []


    def push(self, new_item):
        self.__items.append(new_item)


    def pop(self):
        return self.__items.pop()

    def get(self):
        return self.__items[-1]

    def __str__(self):
        return str(self.__items)

    def __ne__(self, other):
        return self.__items == other

    def __eq__(self, other):
        return self.__items == other

    def __len__(self):
        return len(self.__items)




x = "(3+4) * 2 / ((1-9) + (12-4))"
def is_balanced(equation):
    stack = Stack()

    for c in equation:
        if c == "(":
            stack.push(c)
            print(stack)

        elif c == ")":
            if not stack:
                return False
            stack.pop()

            print(stack)
    return len(stack) == 0

result  = is_balanced(x)
print("Result", result)


