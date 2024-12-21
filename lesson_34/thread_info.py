import threading

def who_is_thread():
    current_thread = threading.current_thread()
    print(f"Thread name: {current_thread.name}")
    print(f"Thread ID: {current_thread.ident}")
    print(f"Thread IsDaemon: {current_thread.daemon}")
    print("\n")




threads = [threading.Thread(target=who_is_thread, name=f"My Thread Name #{i+1}") for i in range(5)]
print("Waiting for thread end!")
for thread in threads:
    thread.start()

for thread in threads:
    thread.join()


print("END OF CODE")

current_thread = threading.current_thread()
print(f"Thread name: {current_thread.name}")
print(f"Thread ID: {current_thread.ident}")
print(f"Thread IsDaemon: {current_thread.daemon}")
print("\n")
