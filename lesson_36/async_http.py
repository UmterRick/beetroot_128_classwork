import asyncio
import time

import aiohttp

async def fetch_data(url, session):
    print(f"Fetch {url.split('/')[-1]}")
    async with session.get(url) as response:
        return await response.text()


async def main():
    base_url = "https://jsonplaceholder.typicode.com/posts/"
    posts_ids = range(1, 101)
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_data(base_url + str(i), session) for i in posts_ids]
        results = await asyncio.gather(*tasks)
        for post in results:
            print(post)


start = time.time()
asyncio.run(main())
print(f"Time: {time.time() - start} s")