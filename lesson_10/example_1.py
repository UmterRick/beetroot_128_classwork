# Python: try / except   (Some other languages: try / catch)

# IndexError
# x = []
# print(x[2])

#KeyError
# x = {}
# print(x["key"])

# ValueError
# x = "hduwnq"
# print(int(x))
def connect():
    print("Connected")

def disconnect():
    print("Disconnected")


connect()
l = []
try:
    x = int(input("x:"))
    result = 20 / x
    print(result)
    l.append(x)
    l.append(result)
    print(l[x])
    r = int("RRRRRRRR")
except (ZeroDivisionError, ArithmeticError) :
    print("ZeroDivisionError  was raised, cause x=0")
    raise TypeError

except IndexError as exc:
    print("IndexError was raised check indexes")

except:
    ...

finally:
    print("FINALLY: REQUIRED CODE!!!!")
    disconnect()


print("END OF CODE")

