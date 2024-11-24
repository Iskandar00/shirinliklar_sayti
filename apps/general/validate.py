from django.core.exceptions import ValidationError
from django.utils.translation import get_language


def phone_number_validate(phone_number: str):
    if len(phone_number) != 13 or not phone_number.startswith('+998') or not phone_number[1:].isdigit():
        raise ValidationError('phone number is not valid.')


def field_language(self, field_name):
    return getattr(self, f'{field_name}_{get_language()}')
