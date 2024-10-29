print("START OF CODE")
x = 2
assert x == 2, f"{x} are not equal 2"

if not x == 2:
    raise AssertionError(f"{x} are not equal 2")
print("END IF CODE")
