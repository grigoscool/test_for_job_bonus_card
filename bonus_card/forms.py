from django.forms import ModelForm
from django import forms

from .models import BonusCard


class BonusCardForm(ModelForm):
    serial_num = forms.IntegerField(help_text='только 4х значные')
    class Meta:
        model = BonusCard
        fields = ['serial_num', 'card_num', 'date_end']


