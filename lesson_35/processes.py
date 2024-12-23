import multiprocessing
import os

def process_target(arg_1, arg_2):
    print(f"Execute in process {arg_1} and {arg_2} received (we are in {os.getpid()})")

new_process = multiprocessing.Process(target=process_target, args=("Arg 1", "Arg 2"))

print("Start")
print(f"Main process {os.getpid()}")

new_process.start()
new_process.join()
print("End")