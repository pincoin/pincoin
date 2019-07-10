from django.urls import path

from . import views

urlpatterns = [
    path('blocks', views.BlockchainListView.as_view(), name='blockchain-list'),
]
