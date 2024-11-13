def fib_gen():
    a = 0
    b = 1
    while True:
        x, y = 10, 20
        yield a
        a, b = b, a + b


fib_gen_obj = fib_gen()
for _ in range(27):
    fib_num = next(fib_gen_obj)
    print(fib_num)



