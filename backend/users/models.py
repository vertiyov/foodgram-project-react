from django.contrib.auth.models import AbstractUser
from django.core.validators import MinLengthValidator, RegexValidator
from django.db import models
from django.contrib.auth.validators import UnicodeUsernameValidator
from foodgram.settings import NAME_MAX_LENGTH, PASSWORD_MAX_LENGTH


class User(AbstractUser):
    first_name = models.CharField(
        'First name',
        max_length=NAME_MAX_LENGTH,
        validators=[
            RegexValidator(
            regex='^[A-Za-zА-Яа-я]*$',
            message='Разрешено использовать только буквы',
            code='invalid_first_name'),
        ]
    )
    last_name = models.CharField(
        'Last name',
        max_length=NAME_MAX_LENGTH,
        validators=[
            RegexValidator(
                regex='^[A-Za-zА-Яа-я]*$',
                message='Разрешено использовать только буквы',
                code='invalid_last_name'),
        ]
    )
    email = models.EmailField(
        'Email',
        unique=True,
    )
    username = models.CharField(
        'Username',
        max_length=NAME_MAX_LENGTH,
        unique=True,
        validators=[MinLengthValidator(3), UnicodeUsernameValidator()]
    )
    password = models.CharField(
        'Password',
        max_length=PASSWORD_MAX_LENGTH,
        unique=True,
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
