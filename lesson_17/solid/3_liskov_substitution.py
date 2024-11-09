class Bird:
    def move(self):
        pass


class Seagull(Bird):
    def move(self):
        return "fly"

class Penguin(Bird):
    def move(self):
        return "swim"


class Ostrich(Bird):
    def move(self):
        return "run"




obj = Penguin()


for i in range(4):
    print(f"I {obj.move()} {i} kilometers")




class Payment:
    def process(self, amount):
        return f"{amount}$ processed"


class CashPayment(Payment):
    def process(self, amount):
        return f"{amount}$ processed in cash"


class CardPayment(Payment):
    def process(self, amount):
        raise NotImplementedError("No terminal")



payment_type = CashPayment

payment_type().process(100)

