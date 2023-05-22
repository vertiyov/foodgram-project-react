from django.core.validators import RegexValidator, MinValueValidator, MaxValueValidator
from django.db import models

from users.models import User
from django.conf import settings

from api.core.validators import RegExColorValidator, RegExNameValidator


class Tag(models.Model):
    name = models.CharField(
        'Name',
        max_length=settings.NAME_MAX_LENGTH,
        unique=True,
        validators=[RegExNameValidator]

    )
    slug = models.SlugField(
        'Slug',
        max_length=settings.NAME_MAX_LENGTH,
        unique=True,
    )
    color = models.CharField(
        'Color',
        max_length=settings.COLOR_MAX_LENGTH,
        unique=True,
        validators=[RegExColorValidator]
    )

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    name = models.CharField(
        'Name',
        max_length=settings.NAME_MAX_LENGTH,
        validators=[RegExNameValidator]
    )
    unit = models.CharField(
        'Unit',
        max_length=settings.UNIT_MAX_LENGTH,
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
        max_length=settings.NAME_MAX_LENGTH,
        unique=True,
        validators=[RegExNameValidator]
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
    cooking_time = models.PositiveSmallIntegerField(
        'Cooking time',
        validators=[
            MinValueValidator(
                settings.MIN_COOKING_TIME,
            )
        ],
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
        verbose_name='Ingredient',
        related_name='+'
    )
    amount = models.PositiveSmallIntegerField(
        validators=[
            MinValueValidator(settings.MIN_AMOUNT_VALUE),
            MaxValueValidator(settings.MAX_AMOUNT_VALUE)
        ],
        verbose_name='Количество ингредиентов'
    )
    def __str__(self):
        return f'{self.ingredient} in {self.recipe}. Amount: {self.amount}'


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
        verbose_name='Recipe',
        related_name='+'
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
        verbose_name='Рецепт',
        related_name='+'
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
