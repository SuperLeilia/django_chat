import json
import time

from channels.generic.websocket import AsyncWebsocketConsumer

from . import tasks


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.user_name = self.scope['url_route']['kwargs']['user_name']
        self.room_group_name = 'chatroom'

        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        message = '{0} 已加入聊天室...'.format(self.user_name)
        tasks.send.apply_async(args=[self.room_group_name, {
            'type': 'chat_message',
            'message': message,
            'user_name': '系统'
        }])

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

        message = '{0} 已退出聊天室...'.format(self.user_name)
        tasks.send.apply_async(args=[self.room_group_name, {
            'type': 'chat_message',
            'message': message,
            'user_name': '系统'
        }])

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        u_name = text_data_json['user_name']

        # Send message to room group with latency
        tasks.send.apply_async(args=[self.room_group_name, {
            'type': 'chat_message',
            'message': message,
            'user_name': u_name
        }], countdown=0)

    async def chat_message(self, event):
        message = '\n{0}\t{1}\n{2}'.format(event['user_name'], time.strftime('%Y-%m-%d %H:%M:%S'), event['message'])

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message,
            'user_name': event['user_name']
        }))
