from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = (
        "id",
        "username",
        "email",
        "first_name",
        "last_name",
        "vk_id",
        "avatar",
    )


admin.site.register(CustomUser, CustomUserAdmin)
