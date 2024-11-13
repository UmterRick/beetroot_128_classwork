def gen_with_send():
    count = 0
    try:
        while True:

            n = yield count
            print(f"n = {n}")
            if n is None:
                print("n is None")
                break
            count += n
    except ConnectionError:
        ...


gen_obj = gen_with_send()
i = next(gen_obj)
print(i)
i = gen_obj.send(11)
print(i)

i = gen_obj.send(30)
print(i)

gen_obj.throw(ValueError, "djhsajdasn")


class VladCollectionList:
    ...


my_list = VladCollectionList()

for i in my_list:
    ...

print(my_list[11])
print(my_list[0])
