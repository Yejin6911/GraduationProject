from channels.generic.websocket import WebsocketConsumer
import json
from asgiref.sync import async_to_sync
from django.db.models.signals import post_save
from django.dispatch import receiver
from channels.layers import get_channel_layer
from .models import Alarm

@receiver(post_save, sender=Alarm)
def announce_likes(sender, instance, created, **kwargs):
    if created:
        channel_layer=get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            "shares", {
                "type": "share_message",
                "longitude": instance.longitude,
                "latitude": instance.latitude,
                "address": instance.address,
                "location_pk":instance.location_pk,
                "station":instance.station,
            }
        )



class UserTestConsumer(WebsocketConsumer):

    def connect(self):
        self.groupname="shares"
        self.accept()

        async_to_sync(self.channel_layer.group_add)(
            self.groupname,
            self.channel_name
        )

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(
            self.groupname,
            self.channel_name
        )

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        longitude = text_data_json['longitude']
        latitude = text_data_json['latitude']
        address = text_data_json['address']
        location_pk = text_data_json['location_pk']
        station = text_data_json['station']

        async_to_sync(self.channel_layer.group_send)(
            self.groupname,
            {
                'type': 'share_message',
                'longitude': longitude,
                'latitude':latitude,
                'address':address,
                "location_pk":location_pk,
                "station":station,
            }
        )

    # Receive message from room group
    def share_message(self, event):
        latitude = event['latitude']
        longitude = event['longitude']
        address = event['address']
        location_pk = event['location_pk']
        station=event['station']
        # Send message to WebSocket
        self.send(text_data=json.dumps({
            'latitude': latitude,
            'longitude':longitude,
            'address': address,
            "location_pk":location_pk,
            "station":station,
        }))
        print(latitude, longitude,address, location_pk, station)