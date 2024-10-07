import random

random_list = []
while len(random_list) < 10:
    random_list.append(random.randint(-100, 100))

print(random_list)