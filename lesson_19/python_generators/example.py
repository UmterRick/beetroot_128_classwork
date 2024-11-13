def generator_example(limit):
    count = 0
    print("BEFORE WHILE")
    while count < limit:
        print("BEFORE YIELD 1")
        yield count
        print("AFTER YIELD 1")


        print("BEFORE YIELD 2")
        yield chr(count)
        print("AFTER YIELD 2")


        yield "Hello"
        count += 1

        return

#
# counter = generator_example(10)
# print(counter)
# for i in counter:
#     print(i)
def read_file_chunks():
    with open("/home/umterrick/beetroot/beetroot_128_classwork/lesson_19/python_iterator/my_iterator_2.py") as file:
        while True:
            line = file.readline()
            if not line:
                break
            yield line


def read_file():
    with open("/home/umterrick/beetroot/beetroot_128_classwork/lesson_19/python_iterator/my_iterator_2.py") as file:
        return file.readlines()


for text_line in read_file_chunks():
    print(text_line)