from django.contrib.auth.models import AbstractUser
from django.core.validators import MinLengthValidator
from django.db import models
from .validators import validate_username


class User(AbstractUser):
    first_name = models.CharField(
        'First name',
        max_length=80,
        blank=False,
        null=False,
    )
    last_name = models.CharField(
        'Last name',
        max_length=80,
        blank=False,
        null=False,
    )
    email = models.EmailField(
        'Email',
        max_length=255,
        unique=True,
        blank=False,
        null=False,
    )
    username = models.CharField(
        'Username',
        max_length=40,
        unique=True,
        blank=False,
        null=False,
        validators=[MinLengthValidator(3), validate_username]
    )
    password = models.CharField(
        'Password',
        max_length=255,
        unique=True,
        blank=False,
        null=False,
    )

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.username


class Subscribe(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='subscriber',
        verbose_name='Subscriber'
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='subscribing',
        verbose_name='Subscribing'
    )

    class Meta:
        verbose_name_plural = 'Подписки на авторов'
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'author'],
                name='unique_subscribe'
            )
        ]
