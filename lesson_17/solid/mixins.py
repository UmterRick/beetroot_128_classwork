class CameraModuleMixin:
    def take_a_photo(self):
        print("Cheeese!")



class DisplayModuleMixin:
    def show_picture(self):
        print("Home screen")


class Phone:
    def __init__(self, model, year):
        self.model = model
        self.year = year

    def call(self):
        ...

    def answer_call(self):
        ...

    def decline_call(self):
        ...

class LoggingMixin:

    def send_logs(self):
        data = self.__dict__

        print(data)

class SmartPhone(Phone, CameraModuleMixin, DisplayModuleMixin, LoggingMixin):
    ...



class SportCar(LoggingMixin):
    def __init__(self, engine, model, mark, year):
        ...



iphone = SmartPhone(16, 2024)
iphone.send_logs()
LoggingMixin().send_logs()
