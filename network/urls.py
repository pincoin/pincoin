from django.urls import path

from . import views

urlpatterns = [
    path('websocket-test-client', views.WebsocketTestClientView.as_view(), name='websocket-test-client'),
    path('peers', views.PeerView.as_view(), name='blockchain-peer-list'),
]
