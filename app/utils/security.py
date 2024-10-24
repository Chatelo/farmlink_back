from functools import wraps
from flask import jsonify, request, current_app
import jwt
from datetime import datetime, timedelta
from flask_security import verify_password
from app.models.user import User
import re
from typing import Optional, Tuple
import time
import redis

# Initialize Redis for rate limiting
redis_client = redis.Redis(host='localhost', port=6379, db=0)

def generate_token(user_id: int) -> str:
    """Generate JWT token for user authentication."""
    payload = {
        'exp': datetime.utcnow() + timedelta(days=1),
        'iat': datetime.utcnow(),
        'sub': user_id
    }
    return jwt.encode(
        payload,
        current_app.config['SECRET_KEY'],
        algorithm='HS256'
    )

def verify_token(token: str) -> Optional[dict]:
    """Verify JWT token and return payload if valid."""
    try:
        payload = jwt.decode(
            token,
            current_app.config['SECRET_KEY'],
            algorithms=['HS256']
        )
        return payload
    except jwt.ExpiredSignatureError:
        return None
    except jwt.InvalidTokenError:
        return None

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