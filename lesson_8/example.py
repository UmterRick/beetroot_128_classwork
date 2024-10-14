def my_function():
    print("Hello")
    print("My Name is Python")
    print("You print in from my_function")
    print()



print("START")
my_function() # function call

# for i in range(20):
#     my_function()

print(type(my_function()))
print(type(my_function))

a_outside_function = "HI from FILE"
b = 99

def number_input(message):
    # scope/namespace
    # a_inside_function = "HI from function"
    # b = 10
    # print(b)
    # print(a_inside_function)
    # print(a_outside_function)
    x = input(message)
    if x.isdigit():
        x = int(x)
        print(f"Your number is: {x}")
    else:
        print("Its not a number")

    return x




print("-----" * 30, "\n\n\n\n\n")


print(a_outside_function)
# print(a_inside_function) # ERROR

function_result = number_input("number_input call: ")
print(function_result, "Type: ", type(function_result))


# number_input("Another Message: ")


print("END")

