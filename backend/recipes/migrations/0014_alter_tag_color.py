# Generated by Django 3.2 on 2023-05-21 01:09

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0013_alter_tag_color'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='color',
            field=models.CharField(max_length=7, unique=True, validators=[django.core.validators.RegexValidator(code='invalid_color', regex='^#?([0-9a-f]{6}|[0-9a-f]{3})$')], verbose_name='Color'),
        ),
    ]