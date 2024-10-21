from time import sleep

file = open("data.txt", 'r')
print(file)
print(type(file))

# file_content = file.read()
# print(file_content)
# print(type(file_content))
print("===" * 30)

file_content = file.read(10)
print(file_content)
print("-----" * 5)
file_content = file.read(10)
print(file_content)
print("-----" * 5)

file_content = file.read(10)
print(file_content)
print("-----" * 5)

file_content = file.read(10)
print(file_content)


file.close()

file = open("data.txt", 'r')
file_lines = file.readlines()
print(file_lines)


file = open("data.txt")
file_line = file.readline()
print(file_line)
print("-----" * 5)
file_line = file.readline()
print(file_line)
print("-----" * 5)
file_line = file.readline()
print(file_line)
print("-----" * 5)
file_line = file.readline()
print(file_line)
print("-----" * 5)
file_line = file.readline()
print(file_line)
print("-----" * 5)
file_line = file.readline()
print(file_line)
print("-----" * 5)
file_line = file.readline()
print(file_line)
print("-----" * 5)
file_line = file.readline()
print(file_line)
print("-----" * 5)
file_line = file.readline()
print(file_line)

print("=========")
file_2 = open("data.txt")
c = file_2.readline()
print(c)
sleep(13)
file_2 = open("data.txt")
print(file_2.read())

