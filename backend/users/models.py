from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    first_name = models.CharField(
        verbose_name='Имя',
        max_length=80,
        blank=False,
        null=False,
    )
    last_name = models.CharField(
        'Фамилия',
        max_length=80,
        blank=False,
        null=False,
    )
    email = models.EmailField(
        'Электронная почта',
        max_length=255,
        unique=True,
        blank=False,
        null=False,
    )
    username = models.CharField(
        'Логин',
        max_length=40,
        unique=True,
        blank=False,
        null=False,
    )
    password = models.CharField(
        'Пароль',
        max_length=100,
        unique=True,
        blank=False,
        null=False,
    )

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.username
