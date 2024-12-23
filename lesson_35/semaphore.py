# Semaphore
import time
from multiprocessing import Process, Semaphore
import random


def process_target(current_semaphore: Semaphore, process_id):
    print(f"\nProcess({process_id}) wait from acquire semaphore")
    with current_semaphore:
        print(f"Process({process_id}) works on task... ")
        time.sleep(random.randint(2, 5))
        print(f"Process({process_id}) release semaphore\n")

    ...
    ...
    ...



my_semaphore = Semaphore(100)

processes = []

for i in range(10):
    process = Process(target=process_target, args=(my_semaphore, i+1))
    processes.append(process)
    process.start()

for p in processes:
    p.join()