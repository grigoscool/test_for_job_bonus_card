from django.core.exceptions import ValidationError


def validate_serial_num(value):
    if 1000 <= value <= 9999:
        return value
    else:
        raise ValidationError('серийник должен быть 4х значным')