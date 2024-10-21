try:

    file = open("data_4.txt", "r")
    print(file.tell())
    file.write("New content 4\n")
except FileNotFoundError:
    open("data_4.txt", "x")