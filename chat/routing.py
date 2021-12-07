from django.conf.urls import re_path
from chat.consumers import ChatConsumer

websocket_urlpatterns = [
    re_path(r'^ws/chat/(?P<user_name>[^/]+)/$', ChatConsumer.as_asgi()),
]