class Bird:
    def fly(self):
        print("I believe I can fly")

    def bite(self):
        print("Dzob")


class Fish:
    def swim(self):
        print("Bul bul bul")

    def bite(self):
        print("----")


class AnimalWithLegs:
    def walk(self):
        print("Walk walk walk")

    def bite(self):
        print("Punch")


class Duck(Bird, AnimalWithLegs, Fish):

    def bite(self):
        print("Dzob and punch")


donald = Duck()

donald.walk()
donald.fly()
donald.swim()
donald.bite()

# MRO
# Duck.__mro__

donald_2 = Duck()
donald_2.bite()
