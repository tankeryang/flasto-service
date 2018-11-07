from functools import wraps
from flask import request


def authorized(func):
    """验证Header的token"""
    @wraps(func)
    def decorator(*args, **kwargs):
        token = None
        
        if 'X-API-KEY' in request.headers:
            token = request.headers['X-API-KEY']
            
            if token == 'Trendy_Crm123':
                return func(*args, **kwargs)
            else:
                return dict(message="Token wrong!"), 401
        else:
            return dict(message="Token is missing!"), 401
        
    return decorator
