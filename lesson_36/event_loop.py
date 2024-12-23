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
    task_1 = asyncio.create_task(task_one())
    task_2 = asyncio.create_task(task_two())


    await task_1
    await task_2

asyncio.run(main())
