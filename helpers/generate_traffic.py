import asyncio
import aiohttp
import time

url = "https://a9de-102-88-69-214.ngrok-free.app/unprotected"
num_requests = 10000  # Total number of requests to send
concurrent_requests = 50  # Number of concurrent requests

async def fetch(session):
    try:
        async with session.get(url) as response:
            status = response.status
            print(f"Status Code: {status}")
    except aiohttp.ClientError as e:
        print(f"Request failed: {e}")

async def generate_traffic():
    start_time = time.time()
    tasks = []

    async with aiohttp.ClientSession() as session:
        for _ in range(num_requests):
            task = asyncio.ensure_future(fetch(session))
            tasks.append(task)
            if len(tasks) >= concurrent_requests:
                await asyncio.gather(*tasks)
                tasks = []

        if tasks:
            await asyncio.gather(*tasks)

    end_time = time.time()
    print(f"Completed {num_requests} requests in {end_time - start_time:.2f} seconds")

if __name__ == "__main__":
    asyncio.run(generate_traffic())
