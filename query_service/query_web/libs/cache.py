from flask_caching import Cache


cache = Cache(config=dict(
    CACHE_TYPE='redis',
    CACHE_REDIS_HOST='redis',
    CACHE_REDIS_PORT=18879,
    CACHE_REDIS_DB=2
))