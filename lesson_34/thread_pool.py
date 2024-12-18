import threading
import time
from concurrent.futures import ThreadPoolExecutor


def handle_file_task(file_name):
    thread = threading.current_thread()
    print(f"Processing {file_name} start in {thread.name}({thread.ident})")
    time.sleep(1)
    print(f"Processing {file_name} finished!")
    print("\n\n\n")


files = [f"file_{i+1}.txt" for i in range(200)]
with ThreadPoolExecutor(max_workers=200) as executor:
    executor.map(handle_file_task,files)


