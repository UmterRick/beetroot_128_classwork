import threading
import time

counter = 0
lock = threading.Lock()

def increment_counter():
    global counter
    for _ in range(100000):
        lock.acquire()

        temp = counter
        # time.sleep(0.000011)
        counter = temp + 1

        lock.release()

def decrement_counter():
    global counter
    for _ in range(100000):
        with lock:
            temp = counter
            # time.sleep(0.00001)
            counter = temp - 1


threads = [threading.Thread(target=increment_counter), threading.Thread(target=decrement_counter)]

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()

print(f"Final counter value: {counter}")


