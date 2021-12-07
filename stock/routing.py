from django.conf.urls import re_path
from stock.consumers import StockConsumer

websocket_urlpatterns = [
    re_path(r'^ws/stock/', StockConsumer.as_asgi()),
]