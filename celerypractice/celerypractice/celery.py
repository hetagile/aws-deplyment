import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'celerypractice.settings')

app = Celery('celerypractice')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()
