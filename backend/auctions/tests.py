import io
from PIL import Image
from django.urls import reverse
from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from django.conf import settings
from .models import Auction


class TestAuctionEndpoints(APITestCase):

    def setUp(self):
        self.data = {
            'username': 'testuser1',
            'password': 'superpass1',
            'email': 'testuser@gmail.com'
        }
        self.path_to_test_photo = settings.MEDIA_ROOT + \
            '/images/Screenshot_from_2024-03-13_18-30-35_atQEteP.png'
        self.user_model = get_user_model()
        self.user = self.user_model.objects.create_user(**self.data)
        self.auction_data = {
            "image_url": self.path_to_test_photo,
            "user": self.user,
            "description": "test description",
            "starting_price": 10,
            "auction_duration": 5
        }
        self.auctions = Auction.objects.create(**self.auction_data)
        self.client.post(reverse('login'), data=self.data, format='json')
        self.token = RefreshToken.for_user(self.user)

    def test_retrieve_all_auctions_without_token(self):
        response = self.client.get(reverse('all_auctions'), format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_retrieve_all_auctions_with_token(self):
        self.client.credentials(
            HTTP_AUTHORIZATION=f'Bearer {self.token.access_token}')
        response = self.client.get(reverse('all_auctions'), format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    @staticmethod
    def generate_random_image():
        file = io.BytesIO()
        image = Image.new('RGBA', size=(100, 100), color=(155, 0, 0))
        image.save(file, 'png')
        file.name = 'test.png'
        file.seek(0)
        return file

    def test_create_auction_without_token(self):
        data = {
            "image_url": TestAuctionEndpoints.generate_random_image(),
            "user": self.user.id,
            "description": "test description",
            "starting_price": 10,
            "auction_duration": 5
        }
        response = self.client.post(
            reverse('all_auctions'),
            data=data,
            format='multipart'
        )
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_auction_with_token(self):
        self.client.credentials(
            HTTP_AUTHORIZATION=f'Bearer {self.token.access_token}')
        data = {
            "image_url": TestAuctionEndpoints.generate_random_image(),
            "user": self.user.id,  # Use user ID instead of the user instance
            "description": "test description",
            "starting_price": 10,
            "auction_duration": 5
        }
        response = self.client.post(
            reverse('all_auctions'),
            data=data,
            format='multipart'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_retrieve_auction_detail(self):
        self.client.credentials(
            HTTP_AUTHORIZATION=f'Bearer {self.token.access_token}')
        response = self.client.get(
            reverse(
                'auction_detail', args=(
                    self.auctions.id,)))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_auction_detail_without_token(self):
        response = self.client.get(
            reverse(
                'auction_detail', args=(
                    self.auctions.id,)))
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_delete_auction_detail(self):
        self.client.credentials(
            HTTP_AUTHORIZATION=f'Bearer {self.token.access_token}')
        response = self.client.delete(
            reverse(
                'manage_auction', args=(
                    self.auctions.id,)))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_get_all_user_auctions(self):
        self.client.credentials(
            HTTP_AUTHORIZATION=f'Bearer {self.token.access_token}')
        response = self.client.get(reverse('my_auctions'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Auction.objects.count(), 1)
