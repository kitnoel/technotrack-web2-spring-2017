from __future__ import absolute_import
import os
import datetime
from celery import Celery, shared_task
from celery.schedules import crontab
from django.conf import settings
from django.contrib.auth import get_user_model

from application.email.send import send_daily_mail

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'application.settings')

app = Celery('application')
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


# @shared_task
# def add(x, y):
#     return x + y

@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(
        schedule=crontab(hour=12, minute=0),
        task=daily_mailing
    )


@app.task
def daily_mailing():
    user_ids = get_user_model().objects.exclude(email=u'').values_list('id', flat=True)
    send_mail.chunks(user_ids, 5).apply_async()


@app.task
def send_mail(user_id):
    user = get_user_model().objects.get(id=user_id)
    send_daily_mail(user, datetime.datetime.now().date())
