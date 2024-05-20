import json
import os

import requests
from django.shortcuts import redirect, render
from dotenv import load_dotenv

from accounts.models import CustomUser
from .constants import VK_API_URL, VK_API_VERSION

load_dotenv()


def index(request):
    if request.session.get('user_vk_id', False):
        return redirect(profile)
    return render(request, "places/index.html")


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
            'fields': 'photo_100'
        }
    ).json().get('response')[0]

    first_name = user_info.get('first_name')
    last_name = user_info.get('last_name')
    avatar = user_info.get('photo_100')

    try:
        user = CustomUser.objects.get(vk_id=user_vk_id)
        user.first_name = first_name
        user.last_name = last_name
        user.avatar = avatar
        user.save()
    except CustomUser.DoesNotExist:
        CustomUser.objects.create(
            vk_id=user_vk_id,
            first_name=first_name,
            last_name=last_name,
            avatar=avatar,
        )

    request.session['user_vk_id'] = user_vk_id

    return redirect(profile)


def profile(request):
    user_vk_id = request.session.get('user_vk_id', False)
    if not user_vk_id:
        return redirect(index)
    user = CustomUser.objects.get(vk_id=user_vk_id)
    context = {
        'first_name': user.first_name,
        'last_name': user.last_name,
        'avatar': user.avatar,
    }
    return render(request, "places/profile.html", context)


def logout(request):
    request.session.flush()
    return redirect(index)
