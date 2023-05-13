from django.db import models

from users.models import User


class Tag(models.Model):
    name = models.CharField(
        'Name',
        max_length=80,
        unique=True,
    )
    slug = models.SlugField(
        'Slug',
        max_length=80,
        unique=True,
    )
    color = models.CharField(
        'Color',
        max_length=7,
        unique=True,
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


class Recipe(models.Model):
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='recipes',
        verbose_name='Recipe author',
    )
    name = models.CharField(
        'Name',
        max_length=80,
        unique=True,
    )
    ingredients = models.ManyToManyField(
        Ingredient,
        through='RecipeIngredient',
        verbose_name='Ingredients',
    )
    image = models.ImageField(
        'Image',
        upload_to='recipes_image/',
        blank=True,
    )
    description = models.TextField(
        'Description',
        unique=True,
    )
    tag = models.ManyToManyField(
        Tag,
        verbose_name='Tags',
    )
    time = models.PositiveIntegerField(
        'Cooking time',
    )


class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name='recipe_ingredients',
        verbose_name='Recipe'

    )
    ingredient = models.ForeignKey(
        Ingredient,
        on_delete=models.CASCADE,
        related_name='recipe_ingredients',
        verbose_name='Ingredient'
    )
    amount = models.IntegerField(
        'Amount',
    )


class FavoriteList(models.Model):
    pass


class ShoppingCart(models.Model):
    pass
