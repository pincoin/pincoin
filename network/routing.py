from django.urls import path

from . import consumers

websocket_urlpatterns = [
    path('ws/network/peer', consumers.PeerConsumer),
    path('ws/network/echo', consumers.EchoConsumer),
]