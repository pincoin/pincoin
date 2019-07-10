from django.conf import settings
from django.contrib import admin
from django.urls import (
    path, include
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blockchain/', include('blockchain.urls')),
    path('network/', include('network.urls')),
]

if settings.DEBUG:
    urlpatterns += [
        path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
    ]
