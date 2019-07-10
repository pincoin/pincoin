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

        self.logger.info('joined')
        self.logger.info(dir(self))

        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.channel_group_name,
            self.channel_name
        )

        self.logger.info('disconnected')

    async def receive_json(self, content):
        self.logger.debug(content['peer'])


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
