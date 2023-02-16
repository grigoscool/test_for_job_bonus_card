from django.db import models
from django.db.models import Q


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
    serial_num = models.PositiveIntegerField()
    card_num = models.PositiveIntegerField()
    date_creation = models.DateTimeField(auto_now_add=True)
    date_end = models.DateTimeField()
    date_use = models.DateTimeField(blank=True, null=True)
    balance = models.IntegerField(default=0)
    activate = models.BooleanField(default=False)
    overdue = models.BooleanField(default=False)

    objects = BonusCardManager()

    def __str__(self):
        return f'Card № {self.card_num}'


class Buy(models.Model):
    name = models.TextField()
    bonus_card = models.ForeignKey(
        BonusCard, on_delete=models.SET_NULL, null=True
    )

    def __str__(self):
        return self.name
