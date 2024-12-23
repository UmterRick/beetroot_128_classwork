import random
import time
from multiprocessing import Process, Lock

def process_target(lock: Lock, process_id):
    print(f"\nProcess({process_id}) wait from acquire lock")
    with lock:
        print(f"Process({process_id}) works on task... ")
        time.sleep(random.randint(2, 5))
        print(f"Process({process_id}) release lock\n")

my_lock = Lock()

processes = []

for i in range(10):
    process = Process(target=process_target, args=(my_lock, i+1))
    processes.append(process)
    process.start()

for p in processes:
    p.join()