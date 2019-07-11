import logging

from channels.consumer import AsyncConsumer
from channels.generic.websocket import AsyncJsonWebsocketConsumer


class PeerConsumer(AsyncJsonWebsocketConsumer):
    logger = logging.getLogger(__name__)

    async def connect(self):
        self.logger.info('connected')

        self.channel_group_name = 'peer_group'

        await self.channel_layer.group_add(
            self.channel_group_name,
            self.channel_name
        )

        self.logger.info('joined channel')

        self.logger.debug('scope type: {}'.format(self.scope['type']))
        self.logger.debug('scope path: {}'.format(self.scope['path']))
        self.logger.debug('scope headers: {}'.format(self.scope['headers']))
        self.logger.debug('scope client: {}'.format(self.scope['client']))
        self.logger.debug('scope server: {}'.format(self.scope['server']))
        self.logger.debug(self.channel_name)

        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.channel_group_name,
            self.channel_name
        )

        self.logger.info('left channel and disconnected')

    async def receive_json(self, content):
        await self.channel_layer.group_send(
            self.channel_group_name,
            {
                'type': 'message',
                'message': content['uri'],
                'channel': self.channel_name,
            }
        )

    async def message(self, event):
        if event['channel'] != self.channel_name:
            await self.send(text_data=event['message'])


class EchoConsumer(AsyncConsumer):
    logger = logging.getLogger(__name__)

    async def websocket_connect(self, event):
        self.logger.info('connected from client')
        await self.send({
            "type": "websocket.accept",
        })

    async def websocket_receive(self, event):
        self.logger.info('received message')
        await self.send({
            "type": "websocket.send",
            "text": event["text"],
        })

    async def websocket_disconnect(self, event):
        self.logger.info('disconnected')
