def func():
    return 12


def func_2():
    return 32


def main(user_input):
    value = int(user_input)
    if value < 0:
        result = func
    else:
        result = func_2
    return result


x = main(input("Value: "))
print(x)
print(x())


def show_google():
    ...


def show_youtube(user):
    ...

def how_to_show_site(url, **kwargs):
    if url == "google.com":
        return show_google

    elif url == "youtube.com":
        return show_youtube


def outer():
    def inner():
        ...


get_site =  how_to_show_site("youtube.com")
get_site()


