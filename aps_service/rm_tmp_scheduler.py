import os
import shutil
from apscheduler.schedulers.background import BackgroundScheduler


PATH = '/opt/flasto-service/query_service/tmp/'


def job():
    if os.path.exists(PATH):
        shutil.rmtree(PATH)
        os.mkdir(PATH)
        print('rm success')
    else:
        os.mkdir(PATH)
        print('mkdir success')


if __name__ == '__main__':
    scheduler = BackgroundScheduler()
    scheduler.add_job(job, trigger='cron', hour='0', minute='0', second='0')
    
    scheduler.start()
    
    try:
        while True:
            pass
    except(KeyboardInterrupt, SystemExit):
        scheduler.shutdown()