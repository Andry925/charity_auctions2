from django.urls import reverse
from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase
from rest_framework import status
from rest_framework.authtoken.models import Token


class TestAuctionEndpoints(APITestCase):

    def setUp(self):
        data = {
            'username': 'testuser1',
            'password': 'superpass1',
            'email': 'testuser@gmail.com'
        }
        self.user = get_user_model()
        self.client.post(reverse('register'), data=data, format='json')
        self.client.post(reverse('login'), data=data, format='json')
        self.token = Token.objects.get(user__username='testuser1')

    def test_retrieve_all_auctions(self):
        response = self.client.get(reverse('all_auctions'), format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
