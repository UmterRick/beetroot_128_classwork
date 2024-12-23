import asyncio
import time


def sync_func():
    print("I am sync")
    return 1

async def async_func():
    print("I am async")
    return 1

async def fetch_data(url = "Hello.com"):
    print(f"Fetch data from {url}")
    await asyncio.sleep(5)
    print(f"fetch completed")
    return {"data": 100}


async def main():
    data = await fetch_data("world.com")
    print(data)
    return data.values()

# async <-> await
result = asyncio.run(main())
print(result)