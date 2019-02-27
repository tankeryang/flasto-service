#!/usr/bin/env bash
docker run --network emr_gw_redis --network-alias redis \
-v /srv/redis/etc:/usr/local/etc/redis \
-v /srv/redis/data:/data \
-p 18879:6379 \
--name redis -d redis \
redis-server --appendonly yes