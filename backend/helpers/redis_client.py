import os
import redis

# use redis url
redis_url = os.getenv('REDIS_URL')
redis_client = redis.StrictRedis.from_url(redis_url, decode_responses=True)
