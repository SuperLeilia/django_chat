from asgiref.sync import async_to_sync
from celery import shared_task
from channels.layers import get_channel_layer

channel_layer = get_channel_layer()

@shared_task
def send(channel_name, message_dict):
    return async_to_sync(channel_layer.group_send)(channel_name, message_dict)
