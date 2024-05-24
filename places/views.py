from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseForbidden
from django.shortcuts import get_object_or_404, redirect, render, reverse
from dotenv import load_dotenv
from django.views import generic
from django.contrib import messages

from accounts.models import CustomUser
from places.forms import PlaceForm
from places.models import Place

load_dotenv()


def index(request):
    if request.user.is_superuser:
        logout(request)
    if isinstance(request.user, CustomUser):
        return redirect(profile)
    return render(request, "places/index.html")


@login_required
def profile(request):
    user = request.user

    places = Place.objects.filter(author=user)

    form = PlaceForm()

    context = {
        'user': user,
        'places': places,
        'form': form,
    }
    return render(request, "places/profile.html", context)


@login_required
def sign_out(request):
    logout(request)
    return redirect(index)


@login_required
def edit_place(request, place_id=None):
    if place_id:
        place = get_object_or_404(Place, pk=place_id)

        if place.author != request.user:
            return HttpResponseForbidden()
    else:
        place = Place(author=request.user)

    form = PlaceForm(request.POST or None, instance=place)

    if request.POST and form.is_valid():
        form.save()
    return redirect(request.META.get('HTTP_REFERER'))


class PlaceDetailView(LoginRequiredMixin, generic.DetailView):
    model = Place
    template_name = "places/place.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = PlaceForm(instance=self.get_object())
        return context
