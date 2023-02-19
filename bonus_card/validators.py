from django.core.exceptions import ValidationError
from django.utils import timezone


def validate_serial_num(value):
    if 1000 <= value <= 9999:
        return value
    else:
        raise ValidationError('серийник должен быть 4х значным')


def validate_date_end_not_in_past(value):
    if value < timezone.now() + timezone.timedelta(days=30):
        raise ValidationError('end time less per month')
    return value


def validate_date_end_not_gt_1year(value):
    if value > timezone.now() + timezone.timedelta(days=365):
        raise ValidationError('Not longer 1 year')
    return value
