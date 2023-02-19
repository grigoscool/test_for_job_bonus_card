from django.core.exceptions import ValidationError
from django.test import TestCase
from django.utils import timezone

from bonus_card.models import BonusCard


class ValidatorTestCase(TestCase):
    def test_validator_serial_num(self):
        for i in range(1000, 10_000, 500):
            item = BonusCard(serial_num=i)
            self.assertRaises(ValidationError, item.full_clean)

    def test_validator_date_end_not_in_past(self):
        for i in range(31, 365, 24):
            item = BonusCard(
                date_end=timezone.now() + timezone.timedelta(days=i))
            self.assertRaises(ValidationError, item.full_clean)

    def test_validate_date_end_not_gt_1year(self):
        item = BonusCard(
            date_end=timezone.now() + timezone.timedelta(days=300))
        self.assertRaises(ValidationError, item.full_clean)
