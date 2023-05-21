from django.core.validators import RegexValidator, MinValueValidator
from django.db import models

from users.models import User
from foodgram.settings import NAME_MAX_LENGTH, COLOR_MAX_LENGTH, UNIT_MAX_LENGTH


class Tag(models.Model):
    name = models.CharField(
        'Name',
        max_length=NAME_MAX_LENGTH,
        unique=True,
    )
    slug = models.SlugField(
        'Slug',
        max_length=NAME_MAX_LENGTH,
        unique=True,
    )
    color = models.CharField(
        'Color',
        max_length=COLOR_MAX_LENGTH,
        unique=True,
        validators=[
            RegexValidator(
                regex='^#(?:[0-9a-fA-F]{3}){1,2}$',
                code='invalid_color'),
        ]
    )

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    name = models.CharField(
        'Name',
        max_length=NAME_MAX_LENGTH,
    )
    unit = models.CharField(
        'Unit',
        max_length=UNIT_MAX_LENGTH,
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
        max_length=NAME_MAX_LENGTH,
        unique=True,
    )
    ingredients = models.ManyToManyField(
        Ingredient,
        through='RecipeIngredient',
        verbose_name='ingredients',
        related_name='ingredients'
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
        verbose_name='Ingredient'
    )
    amount = models.IntegerField(
        validators=[MinValueValidator(1)],
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
