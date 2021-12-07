from django_celery_beat.models import PeriodicTask, IntervalSchedule
from django.core.exceptions import ObjectDoesNotExist
import json
from datetime import datetime, timedelta


# Cron tasks
def generate_cron_task(task_name, task_location, channel_name, stock_code):
    try:
        task = PeriodicTask.objects.get(name=task_name)
        task.args=json.dumps([channel_name, stock_code])
        task.save()
    except ObjectDoesNotExist:
        create_task(task_name, task_location, channel_name, stock_code)


def create_task(task_name, task, channel_name, stock_code):
    schedule, created = IntervalSchedule.objects.get_or_create(
        every=2,
        period=IntervalSchedule.SECONDS,
    )
    PeriodicTask.objects.create(
        interval=schedule,  # Use interval object
        name=task_name,
        task=task,
        args=json.dumps([channel_name, stock_code]),  # parameters
        expires=datetime.now() + timedelta(minutes=60)
    )


def end_cron_task(task_name):
    task = PeriodicTask.objects.get(name=task_name)
    if task is not None:
        task.enabled = False
        task.save()
        task.delete()
