import json

from channels.generic.websocket import AsyncWebsocketConsumer

from . import tasks


class StockConsumer(AsyncWebsocketConsumer):
    room_group_name = 'chatroom'

    async def connect(self):
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )
        pass

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        tasks.send.apply_async(args=[self.room_group_name, {
            'type': 'stock_message',
            'message': message
        }])

    async def stock_message(self, event):
        if '停止' in event['message']:
            message = '\n{0}'.format(event['message'])
        else :
            message = '\n{0}\t{1}'.format('股票代码为：', event['message'])

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message,
        }))

    async def price_message(self, event):
        message = '\n{0}\t{1}:\t{2}'.format('股票', event['stock_code'], event['price'])

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message,
        }))
