import random
import datetime
import math

# print(math.pi)
#
# x = random.randint(0, 100)
# print(datetime.date.today())
# print(datetime.datetime.now())
#
# print(x)
# y = random.randint(20, 25)
# x = datetime.date.today()


x = random.randint(-10, 10)

counter = 0
while counter <= 20:
    y = random.randrange(20, 30, 2 )
    print(y)
    counter +=1

print("\n\n\n\n\n")
string = "abc"

counter = 0
while counter <= 20:
    x = random.choice(string)
    print(x)
    counter +=1

