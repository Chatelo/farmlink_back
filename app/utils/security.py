from functools import wraps
from flask import jsonify, request
import redis

# Initialize Redis for rate limiting
redis_client = redis.Redis(host='localhost', port=6379, db=0)


def rate_limit(requests: int, window: int):
    """Rate limiting decorator."""
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            key = f"{request.remote_addr}:{request.path}"
            current = redis_client.get(key)

            if current is None:
                redis_client.setex(key, window, 1)
            elif int(current) >= requests:
                return jsonify({'error': 'Rate limit exceeded'}), 429
            else:
                redis_client.incr(key)

            return f(*args, **kwargs)
        return decorated_function
    return decorator
