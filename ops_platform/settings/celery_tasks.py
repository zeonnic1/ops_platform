import os
from celery import Celery
import sys
from logging.handlers import RotatingFileHandler
import logging

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ops_platform.settings.dev')
app = Celery('uric',
             broker='amqp://rabbit:rabbit123@localhost:5672/uric',
             backend='rpc://',
             )
task_acks_late = True
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

if __name__ == '__main__':
    app.start(argv=sys.argv[1:])
