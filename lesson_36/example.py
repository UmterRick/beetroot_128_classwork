import asyncio
import time


async def task_one():
    print("Task 1 Start")
    await asyncio.sleep(1)
    print("Task 1 Finish")


async def task_two():
    print("Task 2 Start")
    await asyncio.sleep(0.5)
    print("Task 2 Finish")

async def main():
    await asyncio.gather(task_one(), task_two())

asyncio.run(main())
