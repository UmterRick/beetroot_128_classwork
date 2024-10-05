# AND / OR

true_1 = 1
true_2 = 1
false_1 = 0
false_2 = 0

and_result = false_2 and false_1
print("AND: ", bool(and_result))

or_result = false_1 or false_2
print("OR: ", bool(or_result))

x = (true_1 or false_2) and true_2 and not false_1
print("X ->", bool(x))

print("not True ->", not True)
print("not False ->", not False)

print("----" * 20)
user_is_authorized = False
user_is_admin = False

if not user_is_authorized:
    print("Please login in your account!")
else:
    print("Hello my dear User")

if user_is_authorized and not user_is_admin:
    print("You dont have permission to do it")

print("----" * 20)


def calculate_expr():
    print(">>> Calculating process...")
    return (4 + 5) - (3 * 3)


if False or calculate_expr():
    print("Calculated?")
else:
    print("We got False result")

print((10 < 5) is True)
