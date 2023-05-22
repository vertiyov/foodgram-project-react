# Generated by Django 3.2 on 2023-05-22 09:04

import api.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_alter_user_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(max_length=80, validators=[api.core.validators.RegExNameValidator], verbose_name='First name'),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(max_length=80, validators=[api.core.validators.RegExNameValidator], verbose_name='Last name'),
        ),
    ]
