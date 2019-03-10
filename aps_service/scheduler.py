import os
import shutil
import redis
from apscheduler.schedulers.blocking import BlockingScheduler


PATH = '/opt/flasto-service/query_service/tmp/'


def rm_tmp():
    """
    删除 tmp 目录下的生成文件
    :return:
    """
    if os.path.exists(PATH):
        shutil.rmtree(PATH)
        os.mkdir(PATH)
    else:
        os.mkdir(PATH)


def rm_redis_keys():
    """
    删除 redis 缓存
    :return:
    """
    r = redis.Redis(host='redis', db=2)
    keys = r.keys()
    r.delete(*keys)


if __name__ == '__main__':
    scheduler = BlockingScheduler()
    scheduler.add_job(rm_tmp, trigger='cron', hour='0', minute='0', second='0')
    scheduler.add_job(rm_redis_keys, trigger='cron', hour='4', minute='0', second='0')
    
    scheduler.start()
