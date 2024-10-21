f = open("data.txt")
print("Before enter", f.closed)
f.__enter__() # dunder -- double underscored
print("After enter", f.closed)
f.__exit__(None, None, None)
print("After Exit", f.closed)

with open("data.txt", "wb+") as file:
    print("Closed? -> ", file.closed)
    content = file.read()
    # number = int(content)
    print("Something with file")

print("Closed? -> ", file.closed)


try:
    file =  open("data.txt")
    content = file.read()
    number = int(content)

except ValueError:
    pass

finally:
    file.close()


# x = 5
# if x > 6:
#     pass
# else:
#     print(x)



f = open("not_existing_file.txt", "r+")
print(f)


