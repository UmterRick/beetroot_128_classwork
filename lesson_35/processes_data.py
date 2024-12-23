import time
from multiprocessing import Process, Queue

def producer(data_queue: Queue):
    data = [0, 2, 4, 6, 8, 10]
    print("Send data to queue")
    for el in data:
        print(f"Put {el} to queue")
        data_queue.put(el)
        time.sleep(0.0001)

def consumer(queue):
    while not queue.empty():
        current_element = queue.get()
        time.sleep(0.0001)
        print(f"Get element from queue: {current_element}")


queue = Queue()
prod_process = Process(target=producer, args=(queue, ))
cons_process = Process(target=consumer, args=(queue, ))

cons_process.start()
prod_process.start()

prod_process.join()
cons_process.join()