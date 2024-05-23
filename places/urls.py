from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("profile/", views.profile, name="profile"),
    path("sign_out/", views.sign_out, name="sign_out"),
    path("add_place/", views.edit_place, name="add_place"),
    path("place/<int:pk>/", views.PlaceDetailView.as_view(), name="place_detail"),
    path("edit_place/<int:place_id>/", views.edit_place, name="edit_place"),
]
