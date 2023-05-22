# Generated by Django 3.2 on 2023-05-22 08:37

import api.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0024_alter_tag_color'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='color',
            field=models.CharField(max_length=7, unique=True, validators=[api.core.validators.RegExColorValidator], verbose_name='Color'),
        ),
    ]
