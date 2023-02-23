from django.core.exceptions import ValidationError
from django import forms

from .models import BonusCard


class BonusCardForm(forms.ModelForm):
    """
    Форма для создания бонусной карты.
    """
    class Meta:
        model = BonusCard
        fields = ['serial_num', 'card_num', 'date_end']
        widgets = {
            'serial_num': forms.TextInput(attrs={'class': 'form-control'}),
            'card_num': forms.TextInput(attrs={'class': 'form-control'}),
            'date_end': forms.TextInput(attrs={'type': 'datetime-local',
                                               'class': 'form-control'})
        }

    def __init__(self, *args, **kwargs):
        super(BonusCardForm, self).__init__(*args, **kwargs)
        self.fields['serial_num'].help_text = 'только 4х значные'
            

    def clean_card_num(self):
        # проверка на номер карты больше 100
        card_num = self.cleaned_data.get('card_num')
        if card_num < 100:
            raise ValidationError('номер карты должен быть более 100')
        return card_num

    def clean(self):
        # проверка что серийник и номер карты не совпадают
        serial_num = self.cleaned_data.get('serial_num')
        card_num = self.cleaned_data.get('card_num')
        if card_num == serial_num:
            raise ValidationError('серийник и номер карты не могут быть равны')
