# print - data out
# input - data in
print("Please input your name")
user_name = input()
print(f"Thanks, {user_name}, your name is {type(user_name)} type")

while True:
    user_age = input("Please provide your age: ")
    if user_age.isnumeric():
        user_age = int(user_age)
        break
    print("ALERT: Use only digits!!!")


print(f"Nice, {user_name}, you are {user_age} years old")

print(f"{user_name} next year you will be {user_age + 1} y.o.")

user_hobbies = input("Hobbies (comma separated): ").split(",")

# for item in enumerate(user_hobbies):
#     print(item)