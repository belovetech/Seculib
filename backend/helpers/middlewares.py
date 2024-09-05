import hashlib
from functools import wraps
from flask import request, jsonify
from helpers.redis_client import redis_client

class RateLimitMiddleware:
    def __init__(self, rate_limit=100, time_window=60):
        self.rate_limit = rate_limit
        self.time_window = time_window
        self.redis_client = redis_client

    def get_client_key(self, client_ip, endpoint):
        raw_key = f"{client_ip}:{endpoint}"
        hashed_key = hashlib.sha256(raw_key.encode()).hexdigest()
        return hashed_key

    def is_rate_limited(self, client_ip, endpoint):
        client_key = self.get_client_key(client_ip, endpoint)
        request_count = self.redis_client.get(client_key)

        if request_count is None:
            self.redis_client.setex(client_key, self.time_window, 1)
            return False

        request_count = int(request_count)

        if request_count >= self.rate_limit:
            return True

        self.redis_client.incr(client_key)
        return False

