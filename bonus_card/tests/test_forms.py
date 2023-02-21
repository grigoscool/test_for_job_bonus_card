from django.test import TestCase

from bonus_card.forms import BonusCardForm


class BonusCardFormTestCase(TestCase):

    def test_serial_num_text_help(self):
        # тестируем работу хелп текста
        form = BonusCardForm()
        self.assertEqual(form.fields['serial_num'].help_text,
                         'только 4х значные')
