from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
from rest_framework import status

from bonus_card.models import BonusCard


class HomeViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        number_of_cards = 5
        for card in range(number_of_cards):
            BonusCard.objects.create(
                serial_num=int(f'123{card}'), card_num=int(f'999{card}'),
                date_end=timezone.now()
            )

    def setUp(self) -> None:
        pass

    def test_home_url(self):
        response = self.client.get('')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_home_access_by_name(self):
        response = self.client.get(reverse('bonus_card:home'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTemplateUsed(response, 'bonus_card/home.html')

    def test_pagination_count(self):
        response = self.client.get('')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(3, len(response.context['cards']))


class DetailViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.card_1 = BonusCard.objects.create(
                serial_num=1234, card_num=9999,
                date_end=timezone.now()
            )

    def setUp(self) -> None:
        pass

    def test_exist_url(self):
        response = self.client.get(f'/card-detail/{self.card_1.pk}/')
        self.assertEqual(status.HTTP_200_OK, response.status_code)
