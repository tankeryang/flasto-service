import os
import gevent.monkey
import multiprocessing

gevent.monkey.patch_all()
project_name = os.path.basename(__file__)
current_file_path = os.path.abspath(__file__)
current_dir_path = os.path.split(current_file_path)[0]

# server mechaincs
chdir = current_dir_path

# log
loglevel = 'debug'
accesslog = '%s/log/%s.access.log' % (current_dir_path, project_name)
access_log_format = '%(t)s %(p)s %(h)s "%(r)s" %(s)s %(L)s %(b)s %(f)s" "%(a)s"'
errorlog = '%s/log/%s.error.log' % (current_dir_path, project_name)

# process naming
proc_name = 'query_service'

# server socket
bind = '0.0.0.0:5678'

# worker process
workers = multiprocessing.cpu_count() * 2 + 1
worker_class = 'gunicorn.workers.ggevent.GeventWorker'
threads = multiprocessing.cpu_count() * 2
