import os
import redis

# use redis url
redis_url = os.getenv('REDIS_URL')

try:
    redis_client = redis.StrictRedis.from_url(redis_url, decode_responses=True)
except Exception as e:
    print(e)
