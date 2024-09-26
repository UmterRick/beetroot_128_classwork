some_text = 'jsdnasjdnasjkdnas'
print("text/string type: ", type(some_text))
new_text = str(12312312)

x = "Hello" + " " + "world" + str(2)
print(x)

y = "Some Text For Example"
print("Original: ", y)
print("---" * 30)
print("some text for example".upper())
print(y.upper())
print(y.isupper())
print(y.lower())
print(y.islower())
print(y.capitalize())
print(y.title())
print(y.istitle())
print(y.swapcase())
print()
print(y)

print("---" * 30)

new_str = "Text to learn STR class !"

transformed_str = new_str.replace("STR", "?")
print(new_str)
print(transformed_str)


print(transformed_str.startswith("Text"))
print(transformed_str.endswith("e"))


print("---" * 30)
print(transformed_str)
print(transformed_str[10])
print(transformed_str[-11])
print(len(transformed_str))
print(transformed_str[22])

print("---" * 30)
numbers_str = "0123456789"
print(numbers_str[-3:])


a = 10
b = 2
print(f"{a} + {b} = ", a + b)

print(numbers_str[4])
# numbers_str[4] = "a"
