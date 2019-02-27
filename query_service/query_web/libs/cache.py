from flask_caching import Cache


cache = Cache(config=dict(
    CACHE_TYPE='redis',
    CACHE_REDIS_HOST='localhost',
    CACHE_REDIS_PORT=6379,
    CACHE_REDIS_DB=2
))