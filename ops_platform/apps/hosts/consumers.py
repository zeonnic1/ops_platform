from channels.generic.websocket import AsyncWebsocketConsumer
import json


class HostStatusConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        await self.channel_layer.group_add(
            "host_status"
            , self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard("host_status", self.channel_name)

    async def host_status_update(self, event):
        await self.send(text_data=json.dumps(event["data"]))
