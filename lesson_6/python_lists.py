#
#
# int array[10] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] - массив
#
#
python_array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, "Hello", 13.45324, None, True, False]
# print(python_array)

new_list = [
    "Text",
    [0, 1, 2, 3, 4, ],
    ["My", "Name", "is", "Vlad"],
    None,
    [True, False, False, True],
    True
]
for element in new_list:
    print(element, "->", id(element))

print("True from inner list: ", id(new_list[4][0]))
print("-----" * 10)
print(True, "->", id(True))
print(False, "->", id(False))
print(None, "->", id(None))



print("-----" * 10)
print(new_list[-2])
print(new_list[1:4:2])

print("-----" * 10)
print()

print("Text_" in new_list)
print(" " in "Hello")
forbidden_symbol = ["*", "-", " ", "#"]
phone = "+38097 5555555"

if '+' not in phone:
    print("........")

for symbol in forbidden_symbol:
    if symbol in phone:
        if symbol == " ":
            print("space cant be in your phone number")
        else:
            print(symbol, "cant be in your phone number")

print(type(new_list))

x = "world 123"
y = list(x)
y_reversed = y[::-1]
x_reversed = '|'.join(y_reversed)
print(x)
print(y)
print(y_reversed)
print(x_reversed)




