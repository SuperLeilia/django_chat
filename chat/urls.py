from chat import views as chat_views
from django.urls import path

urlpatterns = [
    path('room', chat_views.room, name='room'),
]