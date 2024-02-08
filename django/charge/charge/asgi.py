import os

from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path
from charge.consumers import ChargeWebsocket

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'charge.settings')

ws_urlpatterns = [
    path('ws/', ChargeWebsocket.as_asgi(), name='charge-websocket')
]

application = ProtocolTypeRouter({
    'http': get_asgi_application(),
    'websocket': URLRouter(ws_urlpatterns)
})
