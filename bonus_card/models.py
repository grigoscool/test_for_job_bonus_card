from django.db import models
from django.db.models import Q
from django.urls import reverse

from .validators import (validate_serial_num,
                         validate_date_end_not_in_past,
                         validate_date_end_not_gt_1year)


class BonusCardManager(models.Manager):
    def search(self, query=None):
        if query is None or query == '':
            self.get_queriset().none()
        lookups = (
                Q(card_num__icontains=query) |
                Q(serial_num__icontains=query) |
                Q(date_creation__icontains=query) |
                Q(date_end__icontains=query)
        )
        return self.get_queryset().filter(lookups)


class BonusCard(models.Model):
    serial_num = models.PositiveIntegerField(
        validators=[validate_serial_num])
    card_num = models.PositiveIntegerField()
    date_creation = models.DateTimeField(auto_now_add=True)
    date_end = models.DateTimeField(
        verbose_name='end time',
        validators=[validate_date_end_not_in_past,
                    validate_date_end_not_gt_1year])
    date_use = models.DateTimeField(blank=True, null=True)
    balance = models.IntegerField(default=0)
    activate = models.BooleanField(default=False)
    overdue = models.BooleanField(default=False)
    slug = models.SlugField(blank=True, null=True)

    objects = BonusCardManager()

    def __str__(self):
        return f'Card № {self.card_num}'

    def get_absolute_url(self):
        return reverse('bonus_card:detail', kwargs={'pk': self.pk})


class Buy(models.Model):
    name = models.CharField(max_length=100)
    bonus_card = models.ForeignKey(
        BonusCard, on_delete=models.SET_NULL, null=True
    )

    def __str__(self):
        return self.name
