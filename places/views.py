from django.contrib.auth import logout
from django.shortcuts import redirect, render
from dotenv import load_dotenv

from accounts.models import CustomUser

load_dotenv()


def index(request):
    if isinstance(request.user, CustomUser):
        return redirect(profile)
    return render(request, "places/index.html")


def profile(request):
    user = request.user

    if not isinstance(user, CustomUser):
        return redirect(index)
    context = {
        'first_name': user.first_name,
        'last_name': user.last_name,
        'avatar': user.avatar,
    }
    return render(request, "places/profile.html", context)


def sign_out(request):
    logout(request)
    return redirect(index)
