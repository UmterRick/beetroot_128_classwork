class OrderService:
    def create(self):
        ...

    def get_order_status(self):
        ...

    def print_receipt(self):
        ...

    def send_order_info(self):
        ...



# class POrder(OrderService):
#     def send_order_info(self):
#         pass
#
#
# class DOrder(OrderService):
#     def print_receipt(self):
#        pass
#
class OrderCreation:
    def create_order(self):
        ...



class OrderStatus:
    def get_status(self):
        ...


class ReceiptPrinter:
    def print_receipt(self):
        ...





class PhysicalOrder(OrderCreation, ReceiptPrinter):
    def create_order(self):
        return "create_physical"

    def print_receipt(self):
        print("order #3")



class DigitalOrder(OrderCreation, OrderStatus):
    def create_order(self):
        return "create_digital"

    def get_status(self):
        return "In Progress"





class Worker:
    def work(self):
        pass


    def eat(self):
        pass


class Employee(Worker):
    def work(self):
        return "work work work"


    def eat(self):
        return "Eating ..."


class Robot(Worker):
    def work(self):
        return "work beep work beep"

    def eat(self):
        raise NotImplementedError("I am not eating")



class WorkMixin:
    def work(self):
        pass


class EatBreakMixin:
    def eat(self):
        pass


class ChargeMixin:
    def charge(self):
        ...


class NewWorker:
    def work(self):
        pass


class NewEmployee(NewWorker, EatBreakMixin):
    def work(self):
        return "work work work"

    def eat(self):
        return "Eating ..."



class NewRobot(NewWorker, ChargeMixin):
    def work(self):
        return "work beep work beep"


    def charge(self):
        return "charging ... "

