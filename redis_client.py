import os
import redis

redis_host = os.getenv('REDIS_HOST')
redis_port = os.getenv('REDIS_PORT')
redis_client = redis.StrictRedis(host=redis_host, port=redis_port, decode_responses=True)
