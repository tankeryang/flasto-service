from flask_caching import Cache


cache = Cache(config=dict(
    CACHE_TYPE='redis',
    CACHE_REDIS_HOST='10.4.21.175',
    CACHE_REDIS_PORT=18879,
    CACHE_REDIS_DB=2
))