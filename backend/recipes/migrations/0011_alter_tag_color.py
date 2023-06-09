# Generated by Django 3.2 on 2023-05-21 01:01

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0010_auto_20230521_0000'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='color',
            field=models.CharField(max_length=7, unique=True, validators=[django.core.validators.RegexValidator(code='invalid_color', regex='[#]\\d{5}')], verbose_name='Color'),
        ),
    ]
