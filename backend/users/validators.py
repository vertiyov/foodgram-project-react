import re

from django.core.exceptions import ValidationError


def validate_username(username):
    if not bool(re.match(r'^[\w.@+-]+$', username)):
        raise ValidationError(
            'В username используются запрещенные символы'
        )
    return username