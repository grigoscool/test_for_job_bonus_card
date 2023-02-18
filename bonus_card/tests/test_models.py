from django.test import TestCase
from django.utils import timezone

from bonus_card.models import BonusCard, Buy


class BonusCardTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.card_1 = BonusCard.objects.create(
            serial_num=1234, card_num=999,
            date_end=timezone.now()
        )

    def setUp(self) -> None:
        pass

    def test_serial_num_field_label(self):
        field_label = self.card_1._meta.get_field('serial_num').verbose_name
        self.assertEqual('serial num', field_label)

    def test_date_end_field_label(self):
        field_label = self.card_1._meta.get_field('date_end').verbose_name
        self.assertEqual('end time', field_label)

    def test_card_name_method(self):
        expected_name = f'Card № {self.card_1.card_num}'
        self.assertEqual(
            ('Card № ' + str(self.card_1.card_num)), expected_name)

    def test_get_absolute_url(self):
        expected_url = self.card_1.get_absolute_url()
        self.assertEqual('/card-detail/1/', str(expected_url))

    def test_balance_default(self):
        expected_balance = self.card_1.balance
        self.assertEqual(0, expected_balance)

    def test_activate_default(self):
        self.assertFalse(self.card_1.activate)


class BuyTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.buy_1 = Buy.objects.create(name='iphone')

    def setUp(self) -> None:
        pass

    def test_name_max_length(self):
        length = self.buy_1._meta.get_field('name').max_length
        self.assertEqual(100, length)
