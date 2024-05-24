from django import forms
from django.core.exceptions import ValidationError

from places.models import Place


class PlaceForm(forms.ModelForm):
    class Meta:
        model = Place
        fields = ('name', 'description', 'latitude', 'longitude')

        widgets = {
            'name': forms.TextInput(
                attrs={
                    'style': 'min-width: 100%; padding: 6px; outline: none; border-radius: 4px; margin-bottom: 12px;',
                    'placeholder': 'Название'
                }),
            'description': forms.Textarea(
                attrs={
                    'style': 'width: 100%; padding: 6px; outline: none; border-radius: 4px; margin-bottom: 6px;',
                    'rows': 6,
                    'placeholder': 'Описание'
                }),
            'latitude': forms.NumberInput(
                attrs={
                    'class': 'hidden',
                }),
            'longitude': forms.NumberInput(
                attrs={
                    'class': 'hidden',
                }),
        }
