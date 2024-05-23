from django.db import models

from accounts.models import CustomUser


class Place(models.Model):
    author = models.ForeignKey(
        CustomUser,
        verbose_name='Автор',
        on_delete=models.CASCADE,
        related_name='places',
    )

    name = models.CharField(
        verbose_name='Название',
        max_length=200,
    )

    description = models.TextField(
        verbose_name='Описание',
    )

    latitude = models.FloatField(
        verbose_name='Широта',
        max_length=10,
    )

    longitude = models.FloatField(
        verbose_name="Долгота",
        max_length=10,
    )

    class Meta:
        ordering = ['-id']
        verbose_name = 'Место'
        verbose_name_plural = 'Места'

    def __str__(self):
        return self.name
