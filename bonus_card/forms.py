from django.core.exceptions import ValidationError
from django.forms import ModelForm
from django import forms

from .models import BonusCard


class BonusCardForm(ModelForm):
    serial_num = forms.IntegerField(help_text='только 4х значные')

    class Meta:
        model = BonusCard
        fields = ['serial_num', 'card_num', 'date_end']

    def clean_card_num(self):
        # проверка на номер карты больше 100
        card_num = self.cleaned_data.get('card_num')
        if card_num < 100:
            raise ValidationError('номер карты должен быть более 100')
        return card_num

    def clean(self):
        serial_num = self.cleaned_data.get('serial_num')
        card_num = self.cleaned_data.get('card_num')
        if card_num == serial_num:
            raise ValidationError('серийник и номер карты не могут быть равны')
