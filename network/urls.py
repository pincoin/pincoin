from django.urls import path

from . import views

urlpatterns = [
    path('peers', views.PeerView.as_view(), name='blockchain-peer-list'),
]
