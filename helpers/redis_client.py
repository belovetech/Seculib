import os
import redis

redis_host = os.getenv('REDIS_HOST', 'redis')
redis_port = int(os.getenv('REDIS_PORT', 6379))
redis_username = os.getenv('REDIS_USERNAME')
redis_password = os.getenv('REDIS_PASSWORD')
redis_client = redis.StrictRedis(host=redis_host, port=redis_port, username=redis_username, password=redis_password, decode_responses=True)
