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

    def __str__(self):
        return self.name


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

    def __str__(self):
        return self.name


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
    text = models.TextField(
        'Description',
        unique=True,
    )
    tags = models.ManyToManyField(
        Tag,
        verbose_name='Tags',
    )
    cooking_time = models.PositiveIntegerField(
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


class Favorite(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='favorites',
        verbose_name='User',
    )
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name='favorites',
        verbose_name='Recipe',
    )

    class Meta:
        ordering = ['-id']
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'recipe'],
                name='unique_userfavorite_recipe'
            )
        ]
        verbose_name_plural = 'Избранное'


class ShoppingCart(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='carts',
        verbose_name='Пользователь',
    )
    recipe = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        related_name='carts',
        verbose_name='Рецепт',
    )

    class Meta:
        ordering = ['-id']
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'recipe'],
                name='unique_user_recipe_cart'
            )
        ]
        verbose_name = 'Список покупок'
