from django.contrib import admin
from django.contrib.admin import ModelAdmin

from .models import Place


class PlaceAdmin(ModelAdmin):
    model = Place
    list_display = (
        "id",
        "name",
        "description",
        "latitude",
        "longitude",
    )


admin.site.register(Place, PlaceAdmin)
