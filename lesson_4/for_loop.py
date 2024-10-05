"""
for <temporary_variable_name> in <some_collection_of_items>:
    <loop body>
"""

some_str = "Hello World!"
looking_for = "l"

for symbol in some_str:
    print(symbol)
    if symbol == looking_for:
        print(f"We found '{looking_for}'")
        break

for i in range(65, 110):
    symbol = chr(i)
    print(symbol)
    i += 1
    if symbol.isupper():
        print(f"skip {symbol}")
        continue

    print(f"{symbol} is lowercase")
    print("complicated calculations")

