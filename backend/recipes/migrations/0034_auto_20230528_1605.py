# Generated by Django 3.2 on 2023-05-28 16:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0033_alter_recipe_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ingredient',
            old_name='unit',
            new_name='measurement_unit',
        ),
        migrations.AlterField(
            model_name='recipe',
            name='image',
            field=models.ImageField(blank=True, upload_to='recipes/', verbose_name='Image'),
        ),
        migrations.AlterField(
            model_name='recipeingredient',
            name='ingredient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recipeingredients', to='recipes.ingredient', verbose_name='Ingredient'),
        ),
        migrations.AlterField(
            model_name='recipeingredient',
            name='recipe',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recipeingredients', to='recipes.recipe', verbose_name='Recipe'),
        ),
    ]
