import json
import random
from time import sleep

from channels.generic.websocket import WebsocketConsumer
from channels.generic.websocket import AsyncWebsocketConsumer

class ChargeWebsocket(AsyncWebsocketConsumer):
    groups = ["general"]

    async def connect(self):
        await self.accept()

    async def receive(self, text_data=None, type='receive', **kwargs):

        data = {
                'status': text_data["data"]
            }
            
        await self.send(json.dumps(data))

    async def disconnect(self, code):
        print("Socket disconnected with code", code)