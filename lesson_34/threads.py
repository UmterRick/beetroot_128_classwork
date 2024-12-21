import threading

def show_text(text, thread_id):
    for i in range(10):
        print(f"Thread_{thread_id} {i},  {text}")

new_thread = threading.Thread(target=show_text, args=(" ABC ", ), kwargs={})
threads = [threading.Thread(target=show_text, args=(" ABC ", i+1), kwargs={}) for i in range(5)]
print("Waiting for thread end!")
for thread in threads:
    thread.start()

for thread in threads:
    thread.join()

print("END OF CODE", end="\n")

