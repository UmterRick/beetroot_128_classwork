def outer_func():
    x = 100 * 3432

    def inner_func(name):
        print(f"Hello, {name}!")


        def inner_inner():
            return 0

        inner_inner()

    inner_inner()

    inner_func("Vlad")
    inner_func("Vlad")
    inner_func("Vlad")
    inner_func("Vlad")
    inner_func("Vlad")


outer_func()
inner_func()