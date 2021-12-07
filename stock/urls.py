from django.urls import path
from stock import views as stock_views

urlpatterns = [
    path('', stock_views.channel_room, name='stock_channel'),
    path('send_stock_num', stock_views.send_stock_num, name='send_stock_num'),
    path('http_room', stock_views.room_http, name='stock_http'),
    path('channel_room', stock_views.channel_room, name='stock_channel')
]