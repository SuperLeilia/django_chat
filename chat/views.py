from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.safestring import mark_safe
import json

@login_required
def room(request):
    user_name = request.user.username
    user_name_json = mark_safe(json.dumps(user_name))
    return render(request, 'chat/room.html', {
        'user_name_json': user_name_json,
    })

