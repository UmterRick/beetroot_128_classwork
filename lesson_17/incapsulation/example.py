class Person:
    def __init__(self, name: str, status: str | None = None):
        self.__name = name
        self.status = status

    def get_name(self):
        if self.status:
            return f"{self.status.title()} {self.__name.title()}"
        return self.__name

    def get_status(self):
        return self.status

    def set_status(self):
        ...


professor = Person("John Doe", status="professor")
# print(professor.get_name())

student_1 = Person("Leonardo Di Caprio", status="student")
print(student_1.get_name())
student_1.__name = "Will Smith"
print(student_1.get_name())


class EmailHandler:

    def __connect_to_mail_server(self):
        ...

    def send(self, from_address, to_address, content):
        if self.__connect_to_mail_server() == "SUCCESS":
            self.__send()


    def __send(self):
        ...




class Journal:

    def add_note(self):
        ...

    def get_note(self):
        ...

    def edit(self):
        ...

    def delete(self):
        ...

    def send_note_to_email(self, email_address):
        email_handler = EmailHandler().send("", "", self.get_note())


__PRIVATE_TRY_TO_IMPORT = "Hi"