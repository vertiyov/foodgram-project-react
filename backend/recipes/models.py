from django.db import models

from users.models import User

class Recipe(models.Model):
    pass

class Tag(models.Model):
    pass

class Ingredient(models.Model):
    name = models.CharField(
        'Название ингредиента',
        max_length=80,
        blank=False,
        null=False,
    )
    unit = models.CharField(
        'Единица измерения',
        max_length=20,
        blank=False,
        null=False,
    )

class FavoriteList(models.Model):
    pass

class ShoppingCart(models.Model):
    pass

