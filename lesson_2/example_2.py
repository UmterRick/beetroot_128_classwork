# Create own function with print to file
def my_print(*args):
    with open("print_result.txt", "a") as my_file:
        print(*args, sep=" _my_sep_ ", end="\n\n\n", file=my_file)


my_print(1, 1.53289, "3_Pigs", 4, 5, 6, 7, 8, 9)
my_print(1, 2, 3, 4, 5)
