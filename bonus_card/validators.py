from django.core.exceptions import ValidationError
from django.utils import timezone


def validate_serial_num(value):
    # проверка на 4х значность
    if 1000 <= value <= 9999:
        return value
    else:
        raise ValidationError('серийник должен быть 4х значным')


def validate_date_end_not_in_past(value):
    # проверка на дата окончания минмум через месяц
    if value < timezone.now() + timezone.timedelta(days=30):
        raise ValidationError('дата окончания минимум через месяц')
    return value


def validate_date_end_not_gt_1year(value):
    # проерка на дата окончания не более 1 года
    if value > timezone.now() + timezone.timedelta(days=365):
        raise ValidationError('Not longer 1 year')
    return value
