from multiprocessing import cpu_count

bind = '0.0.0.0:8000'
workers = cpu_count() * 2 + 1
worker_class = 'gevent'
max_requests = 1000
forwarded_allow_ips = '*'
reload = True