def create_error():
    print("Error is coming...")
    raise ValueError("This is my error, just for fun!")

# create_error()


def learn_python():
    try:
        l = [1, 2, 3, 4]
        l.reverse()
        return l
    # except IndexError:
    #     print("What have you done!? Its an error")
    finally:
        print("FINALLY -> HELLO i am still here")

x = learn_python()
print(">>>", x)