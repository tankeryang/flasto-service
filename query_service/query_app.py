import os
import shutil
from apscheduler.schedulers.background import BackgroundScheduler
from query_service.query_biz.crm.const import const
from query_service.query_web import create_app


PATH = const.ExportFilePath.PATH


def job():
    if os.path.exists(PATH):
        shutil.rmtree(PATH)
        os.mkdir(PATH)
        print('rm success')
    else:
        os.mkdir(PATH)
        print('mkdir success')


if __name__ == '__main__':
    app = create_app('development')
    
    scheduler = BackgroundScheduler()
    scheduler.add_job(job, trigger='cron', hour='0', minute='0', second='0')
    
    scheduler.start()
    app.run()
