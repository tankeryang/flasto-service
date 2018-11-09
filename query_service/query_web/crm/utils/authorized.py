from functools import wraps
from flask import request

from ..const import Const


def authorized(func):
    """验证Header的token"""
    @wraps(func)
    def decorator(*args, **kwargs):
        if 'X-API-KEY' in request.headers:
            token = request.headers['X-API-KEY']
            
            if token == Const.X_API_KEY:
                return func(*args, **kwargs)
            else:
                return dict(message="Token wrong!", success=False), 401
        else:
            return dict(message="Token is missing!", success=False), 401
        
    return decorator
