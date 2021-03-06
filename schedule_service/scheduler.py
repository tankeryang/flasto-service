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
    r2 = redis.Redis(host='redis', db=2)
    r4 = redis.Redis(host='redis', db=4)
    
    keys2 = r2.keys()
    r2.delete(*keys2)
    
    keys4 = r4.keys()
    r4.delete(*keys4)


if __name__ == '__main__':
    scheduler = BlockingScheduler()
    scheduler.add_job(rm_tmp, trigger='cron', hour='0', minute='0', second='0')
    scheduler.add_job(rm_redis_keys, trigger='cron', hour='4', minute='0', second='0')
    
    scheduler.start()
