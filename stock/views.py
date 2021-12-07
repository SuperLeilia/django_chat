import json

import redis
from django.contrib.auth.decorators import login_required
from django.core.exceptions import BadRequest
from django.http import HttpResponse
from django.shortcuts import render

from . import tasks
from .consumers import StockConsumer


@login_required
def channel_room(request):
    return render(request, 'stock/room_channel.html')


@login_required
def room_http(request):
    return render(request, 'stock/room_http.html')


@login_required
def send_stock_num(request):
    if request.method == 'POST':
        if 'message' in request.POST:
            tasks.send(StockConsumer.room_group_name, request.POST)
            return HttpResponse(json.dumps(request.POST['message'].strip()))
        else:
            raise BadRequest('No message found!')
