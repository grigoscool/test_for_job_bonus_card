from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
from rest_framework import status

from bonus_card.models import BonusCard


class StaticUrlTest(TestCase):
    """Страница доступна по URL."""
    @classmethod
    def setUpTestData(cls):
        cls.card_1 = BonusCard.objects.create(
            serial_num=1234, card_num=9999,
            date_end=timezone.now()
        )

    def test_static_url(self):
        path_row: tuple = ('', '/generate_card/')
        for path in path_row:
            response = self.client.get(path)
            error_name: str = f'No access page: {path}'
            self.assertEqual(
                status.HTTP_200_OK, response.status_code, error_name)

    def test_url_used_correct_template(self):
        url_temp: dict = {
            '': 'bonus_card/home.html',
            '/generate_card/': 'bonus_card/generate_card.html',
        }
        for url, template in url_temp.items():
            response = self.client.get(url)
            error_name: str = f'url {url} expected {template}'
            self.assertTemplateUsed(response, template, error_name)

    def test_dinamic_url(self):
        path_row: tuple = (
            f'/card-detail/{self.card_1.pk}/',
            f'/activate/{self.card_1.pk}/',
            f'/deactivate/{self.card_1.pk}/',
            f'/delete/{self.card_1.pk}/',
        )
        for path in path_row:
            response = self.client.get(path)
            error_name: str = f'No access page: {path}'
            self.assertEqual(
                status.HTTP_200_OK, response.status_code, error_name)


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

    def test_home_access_by_name(self):
        response = self.client.get(reverse('bonus_card:home'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTemplateUsed(response, 'bonus_card/home.html')

    def test_pagination_count(self):
        response = self.client.get('')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(3, len(response.context['cards']))



