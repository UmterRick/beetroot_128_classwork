# if/elif виконувати якщо {умова} вірна

# while  - виконувати поки {умова} вірна

x = 0
counter = 0
while x <= 10:
    # iteration - ітерація
    # start loop
    print(f"Action in a while loop, x = {x}, {counter}")
    counter = counter + 1
    x += 1
    # end loop

print("END OF CODE")
print("\n\n\n")

some_str = "Hello World!"
looking_for = "l"
pointer = 0
last_index = len(some_str)

some_str_lower = some_str.lower()
while pointer < last_index:
    symbol = some_str_lower[pointer]
    # print(symbol)
    if symbol == looking_for:
        print(f"We found '{looking_for}' at index {pointer}")
        break
    pointer += 1

i = 65
while i < 110:
    symbol = chr(i)
    print(symbol)
    i += 1
    if symbol.isupper():
        print(f"skip {symbol}")
        continue

    print(f"{symbol} is lowercase")
    print("complicated calculations")


