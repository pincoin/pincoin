from django.urls import path

from . import consumers

websocket_urlpatterns = [
    path('ws/blockchain/peer', consumers.PeerConsumer),
    path('ws/blockchain/echo', consumers.EchoConsumer),
]