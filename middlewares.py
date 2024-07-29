import time
import hashlib
from flask import request, jsonify
import redis

class RateLimitMiddleware:
    def __init__(self, app, rate_limit=100, time_window=60, redis_host="localhost", redis_port=6379):
        self.app = app
        self.rate_limit = rate_limit
        self.time_window = time_window
        self.redis_client = redis.StrictRedis(host=redis_host, port=redis_port, decode_responses=True)
        self.app.before_request(self.before_request)

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

    def before_request(self):
        client_ip = request.remote_addr
        endpoint = request.path

        if self.is_rate_limited(client_ip, endpoint):
            return jsonify({"error": "Too many requests"}), 429

