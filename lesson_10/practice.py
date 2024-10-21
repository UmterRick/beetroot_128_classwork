import  random


def process(a):
    return 1000 / a

c = 0

while c < 100:
    try:
        x = process(random.randint(-1, 1))
        print(f"x = {x}")
    except (ZeroDivisionError, IndexError):
        print("wait for miracle")
        # sleep(0.1)

    except ValueError as exc:
        print(exc.args)

    finally:
        c += 1

