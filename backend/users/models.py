from django.contrib.auth.models import AbstractUser
from django.core.validators import MinLengthValidator
from django.db import models
from .validators import validate_username


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
        max_length=254,
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
        validators=[MinLengthValidator(3), validate_username]
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
