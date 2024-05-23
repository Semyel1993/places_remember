import json
import os

import requests
from django.contrib.auth import login
from django.shortcuts import redirect
from dotenv import load_dotenv

from .models import CustomUser
from places.views import profile
from constants import VK_API_URL, VK_API_VERSION, VK_AVATAR

load_dotenv()


def auth(request):
    payload_params = request.GET.get('payload')
    payload_json = json.loads(payload_params)
    uuid = payload_json.get('uuid')
    silent_token = payload_json.get('token')
    service_token = os.getenv("SERVICE_TOKEN")

    payload_params = {
        'token': silent_token,
        'access_token': service_token,
        'uuid': uuid,
        'v': VK_API_VERSION,
    }

    exchange_silent_token = requests.get(
        VK_API_URL + 'auth.exchangeSilentAuthToken',
        params=payload_params
    ).json().get('response')

    access_token = exchange_silent_token.get('access_token')
    user_vk_id = exchange_silent_token.get('user_id')
    user_info = requests.get(
        VK_API_URL + 'users.get',
        params={
            'access_token': access_token,
            'v': VK_API_VERSION,
            'fields': VK_AVATAR + ', screen_name'
        }
    ).json().get('response')[0]

    first_name = user_info.get('first_name')
    last_name = user_info.get('last_name')
    screen_name = user_info.get('screen_name')
    avatar = user_info.get(VK_AVATAR)
    try:
        user = CustomUser.objects.get(vk_id=user_vk_id)
        user.first_name = first_name
        user.last_name = last_name
        user.avatar = avatar
        user.save()
    except CustomUser.DoesNotExist:
        user = CustomUser.objects.create(
            username=screen_name,
            vk_id=user_vk_id,
            first_name=first_name,
            last_name=last_name,
            avatar=avatar,
        )

    login(request, user)
    return redirect(profile)
