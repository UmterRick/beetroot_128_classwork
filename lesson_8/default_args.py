from lesson_6.python_lists import new_list


def some_function(a=5, b=7):
    print(a * b)


some_function(b="___---___ ")


def repeat_text(text: str, count: int | float, is_upper: bool) -> str:
    """

    :param text: some str text
    :param count: how many time repeat text
    :param is_upper: bool True or False
    :return: str
    """
    if is_upper:
        text = text.upper()
    return text * int(count)


def some_loop(n_list: list[int | float] | None) -> str | None:

    return n_list

some_loop(n_list=[1, 2, 4, 5, "H"])

x: dict[str, list[int]]


result = repeat_text("Hello ", 5.5, True)
print(result)




