# Generated by Django 3.2 on 2023-05-22 09:04

import api.core.validators
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0025_alter_tag_color'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredient',
            name='name',
            field=models.CharField(max_length=80, validators=[api.core.validators.RegExNameValidator], verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='cooking_time',
            field=models.PositiveSmallIntegerField(validators=[django.core.validators.MinValueValidator(1)], verbose_name='Cooking time'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='name',
            field=models.CharField(max_length=80, unique=True, validators=[api.core.validators.RegExNameValidator], verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='recipeingredient',
            name='amount',
            field=models.PositiveSmallIntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(30)], verbose_name='Количество ингредиентов'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='name',
            field=models.CharField(max_length=80, unique=True, validators=[api.core.validators.RegExNameValidator], verbose_name='Name'),
        ),
    ]
