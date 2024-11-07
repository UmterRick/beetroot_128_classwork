tasks = []

def tasks_executor():
    while tasks:
        task = tasks.pop(0)
        print(f"Get Task({task}) from list")
        task.execute()
        print()


class Task:
    def execute(self):
        pass

class TasksSet:
    def __init__(self):
        self.tasks = []

    def add_task(self, task: Task):
        if not isinstance(task, Task):
            raise TypeError("You can add only tasks here")

        self.tasks.append(task)


class UploadFileTask(Task):
    def __init__(self, file, path):
        self.file = file
        self.path = path

    def execute(self):
         print(f"upload {self.file} to {self.path}")

class SendEmailTask(Task):
    def __init__(self, address, mail):
        self.mail = mail
        self.address = address





    def execute(self):
        print(f"Send {self.mail} to {self.address}")


def create_user(user_name):
    new_task = SendEmailTask(f"{user_name}@mail.com", "Welcome")
    tasks.append(new_task)





for i in range(10):
    create_user(f"user_{i}")


for file in range(20):
    tasks.append(UploadFileTask(f"file_{file}.csv", "Downloads"))

print(tasks)
tasks_executor()


"""
x = {
    "png": PNGHandler,
    "jpeg" : JpegHandler
}
file_type =  file_name.split(".")[-1]
file_handler = x.get(file_type, DefaultFileHandler)


file_handler.open()

"""
card_info = {
    "bank": "mono"
}

class Payment:
    def pay(self):
        pass


class MonoPay(Payment):
    def pay(self):
        print("Go to Mono")


class PrivatPay(Payment):
    def pay(self):
        print("Go to PrivatBank")

class OshadPay(Payment):
    def pay(self):
        print("Go to OshadBank")


bank_dict = {
    "mono": MonoPay,
    "privat": PrivatPay,
    "oshad": OshadPay


}


bank = bank_dict[card_info["bank"]]


# if bank == "mono":
#     .....
#
# elif bank == "privat":
#     .....
#
#
bank.pay()



