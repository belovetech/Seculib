from flask import  jsonify, request
from api.library.views import app_views
import asyncio
import aiohttp
import time

url = 'http://localhost:5050/api/v1/books'

async def fetch(session):
    try:
        async with session.get(url) as response:
            status = response.status
            print(f"Status Code: {status}")
    except aiohttp.ClientError as e:
        print(f"Request failed: {e}")

async def generate_traffic(num_requests=300, concurrent_requests=50):
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
    return end_time - start_time

@app_views.route('/simulate_ddos', methods=['GET', 'POST'])
def simulate_ddos_attack():
    num_requests = 100
    concurrent_requests = 10
    # url = 'https://secure-auth-dos-prevention.onrender.com/api/v1/books'
    if request.method == 'POST':
        num_requests = request.json.get("num_requests", 100)
        concurrent_requests = request.json.get("concurrent_requests", 50)

    asyncio.run(generate_traffic(num_requests, concurrent_requests))
    return jsonify({"message": "Success"}), 200
