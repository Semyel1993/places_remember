from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    vk_id = models.BigIntegerField(unique=True, blank=True, null=True)
    avatar = models.ImageField(
        max_length=255,
        verbose_name='Аватар пользователя',
        upload_to='avatars/',
        blank=True,
    )

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.get_full_name()
