from django.db import models

from users.models import User

class Recipe(models.Model):
    pass

class Tag(models.Model):
    name = models.CharField(
        'Name',
        max_length=80,
        unique=True,
        blank=False,
        null=False,
    )
    slug = models.SlugField(
        'Slug',
        max_length=80,
        unique=True,
        blank=False,
        null=False,
    )
    color = models.CharField(
        'Color',
        max_length=7,
        unique=True,
        blank=False,
        null=False,
    )

class Ingredient(models.Model):
    name = models.CharField(
        'Name',
        max_length=80,
        blank=False,
        null=False,
    )
    unit = models.CharField(
        'Unit',
        max_length=40,
        blank=False,
        null=False,
    )

class FavoriteList(models.Model):
    pass

class ShoppingCart(models.Model):
    pass

