f = open("data.txt")
print(f.tell())
l = f.readline()
print(f.tell())
print(l)

f.seek(0)
content = f.read()
last_index = len(content)


f.seek(last_index-10)
print(f.tell(), "\n")
l_2 = f.read()
print(l_2)



