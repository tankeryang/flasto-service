from functools import wraps
from flask import request, current_app


def authorized(func):
    """验证Header的token"""
    @wraps(func)
    def decorator(*args, **kwargs):
        if 'X-API-KEY' in request.headers:
            token = request.headers['X-API-KEY']
            
            if token == current_app.config['SECRET_KEY']:
                return func(*args, **kwargs)
            else:
                return dict(message="Token wrong!", success=False), 401
        else:
            return dict(message="Token is missing!", success=False), 401
        
    return decorator
