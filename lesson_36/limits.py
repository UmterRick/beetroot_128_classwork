import asyncio
from random import random

from lesson_36.example import task_one

semaphore = asyncio.Semaphore(5)

async def async_task(i):
    async with semaphore:
        print(f"\nTask {i} start")
        await asyncio.sleep(5)
        print(f"Task {i} finish\n")


async def main():
    tasks = [async_task(i) for i in range(50)]
    await asyncio.gather(*tasks)


asyncio.run(main())
