
import os
from flask import Flask, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
from helpers.middlewares import RateLimitMiddleware
from api import app_views


app = Flask(__name__)
CORS(app)


# apply rate limit middleware
RateLimitMiddleware(app, rate_limit=100, time_window=60)

load_dotenv(override=True)
SECRET_KEY = os.getenv('SECRET_KEY')

app.register_blueprint(app_views)


@app.route('/healthz', methods=['GET'])
def healthz():
    print("Health check.")
    return jsonify({'message': 'OK'})


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=3000, debug=True)
