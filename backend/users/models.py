from django.contrib.auth.models import AbstractUser
from django.core.validators import MinLengthValidator, RegexValidator
from django.db import models
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.conf import settings

from api.core.validators import RegExNameValidator


class User(AbstractUser):
    first_name = models.CharField(
        'First name',
        max_length=settings.NAME_MAX_LENGTH,
        validators=[RegExNameValidator]
    )
    last_name = models.CharField(
        'Last name',
        max_length=settings.NAME_MAX_LENGTH,
        validators=[RegExNameValidator]
    )
    email = models.EmailField(
        'Email',
        unique=True,
    )
    username = models.CharField(
        'Username',
        max_length=settings.NAME_MAX_LENGTH,
        unique=True,
        validators=[MinLengthValidator(settings.MIN_USERNAME_LENGTH), UnicodeUsernameValidator()]
    )
    password = models.CharField(
        'Password',
        max_length=settings.PASSWORD_MAX_LENGTH,
    )

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.username


class Subscribe(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='follower',
        verbose_name='Subscriber'
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='following',
        verbose_name='Subscribing'
    )

    class Meta:
        verbose_name_plural = 'Подписки на авторов'
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'author'],
                name='unique_subscribe'
            ),
        models.CheckConstraint(
            check=~models.Q(author=models.F('user')),
            name='forbidden_self_subscribe'
        )
        ]
