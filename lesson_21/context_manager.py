from lesson_11.write_to_file import file_name

with open("") as file:  # enter
    file


# exit


class MyContextManager:
    def __init__(self, filename, mode):
        self.file_name = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        print("2) Enter action")

        self.file = open(self.file_name, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Type:")
        print(exc_type)
        print("Value:")
        print(exc_val)
        print("TraceBack:")
        print(exc_tb)
        print("4) Exit action")
        if exc_type == ValueError:
            print("Save my data or connection")

        self.file.close()


print("1) Before with")
with MyContextManager() as value:
    print(value)
    # raise ValueError("Error message")

    print("3) Inside context manager")

print("5) After with")
