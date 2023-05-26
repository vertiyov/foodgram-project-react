import re

from django.forms import forms


def RegExColorValidator(value):
    regex = '^#([0-9a-fA-F]{3,6})$'
    if re.match(regex, value):
        return value
    else:
        raise forms.ValidationError("Введите корректный  Hex-Code")


def RegExNameValidator(value):
    regex = '^[A-Za-zА-Яа-я]*$'
    if re.match(regex, value):
        return value
    else:
        raise forms.ValidationError("Разрешено использовать только буквы")
