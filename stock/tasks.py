import redis
from asgiref.sync import async_to_sync
from celery import shared_task
from channels.layers import get_channel_layer
from stock.cron_util import generate_cron_task, end_cron_task
import random

channel_layer = get_channel_layer()


@shared_task
def send(channel_name, message_dict):
    async_to_sync(channel_layer.group_send)(channel_name, message_dict)
    if message_dict['message'].strip() == '停止':
        end_cron_task('send_price')
    else:
        generate_cron_task('send_price', 'stock.tasks.send_price', channel_name, message_dict['message'])


@shared_task
def send_price(channel_name, stock_code):
    num = random.uniform(0, 1000)
    print(str(round(num, 2)))
    async_to_sync(channel_layer.group_send)(channel_name, {
        'type': 'price_message',
        'stock_code': stock_code,
        'price': str(round(num, 2))
    })

