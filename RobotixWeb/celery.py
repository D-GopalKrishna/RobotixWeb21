from __future__ import absolute_import, unicode_literals # for python2
import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'RobotixWeb.settings')

BASE_REDIS_URL = os.environ.get('REDIS_URL', 'redis://redis:6379')

app = Celery('RobotixWeb')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

app.conf.broker_url = BASE_REDIS_URL

# this allows you to schedule items in the Django admin.
app.conf.beat_scheduler = 'django_celery_beat.schedulers.DatabaseScheduler'


from celery.schedules import crontab
app.conf.beat_schedule = {
        'every-60-seconds': {
        'task': 'certificate_generation',
        'schedule': 60,
    },
        'every-60-seconds': {
        'task': 'email_certificate',
        'schedule': 60,
    },
    # 'add-every-minute-contrab': {
    #     'task': 'multiply_two_numbers',
    #     'schedule': crontab(hour=7, minute=30, day_of_week=1),
    #     'args': (16, 16),
    # },

}