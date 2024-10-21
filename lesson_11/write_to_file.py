file_name = "data.txt"
file = open(file_name, "r")
file.seek(0)
content = file.read()
last_index = len(content)
file.close()


file = open(file_name, "w+")
# content = file.read()
# print(content)

file.write("Hello!!!\n")
file.writelines(
    [
    "line_1\n",
    "line_2\n",
    "line_3\n",
    "line_4\n",
    "line_5\n",
    ]
)


file = open("data.txt", "w")
print(last_index)
file.seek(last_index)
file.write("New content")