import multiprocessing

bind = 'localhost:8080'
backlog = 2048
workers = multiprocessing.cpu_count()
worker_class = 'sync'
worker_connections = 1000
timeout = 60
keepalive = 2
daemon = False
errorlog = '/Users/robert/Documents/WEBDZ/gunicorn_files/wsgi.error.log'
loglevel = '/Users/robert/Documents/WEBDZ/gunicorn_files/wsgi.access.log'