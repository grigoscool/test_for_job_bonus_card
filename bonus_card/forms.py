from django.forms import ModelForm
from .models import BonusCard


class BonusCardForm(ModelForm):
    class Meta:
        model = BonusCard
        fields = ['serial_num', 'card_num', 'date_end']
