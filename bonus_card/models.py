from django.db import models


class BonusCard(models.Model):
    serial_num = models.PositiveIntegerField()
    card_num = models.PositiveIntegerField()
    date_creation = models.DateTimeField(auto_now_add=True)
    date_end = models.DateTimeField()
    date_use = models.DateTimeField(blank=True, null=True)
    balance = models.IntegerField()
    activate = models.BooleanField(default=False)

    def __str__(self):
        return f'Card № {self.card_num}'
