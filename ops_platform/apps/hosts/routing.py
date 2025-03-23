from django.urls import path
from .consumers import HostStatusConsumer

websocket_urlpatterns = [
    path("ws/host_status/", HostStatusConsumer.as_asgi()),  # WebSocket 路径
]
