from django.test import TestCase
from django.urls import reverse
from rest_framework import status

from bonus_card.models import BonusCard


class HomeViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        pass

    def setUp(self) -> None:
        pass

    def test_home_url(self):
        response = self.client.get('')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_home_access_by_name(self):
        response = self.client.get(reverse('bonus_card:home'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTemplateUsed(response, 'bonus_card/home.html')
