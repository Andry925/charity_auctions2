from django.urls import reverse
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import RefreshToken


class TestAuthentication(APITestCase):

    def setUp(self):
        self.data = {
            "username": "someone1",
            "password": "superpass",
            "email": "some@gmail.com",
        }
        User = get_user_model()
        self.user = User.objects.create_user(**self.data)

    def test_register(self):
        data = {
            "username": "someone2",
            "email": "some2@gmail.com",
            "password": "superpass2"
        }
        response = self.client.post(
            reverse('register'), data=data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_register_existing_user(self):
        response = self.client.post(
            reverse('register'),
            data=self.data,
            format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_login(self):
        response = self.client.post(
            reverse('login'), data=self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_login_with_invalid_credentials(self):
        data = {
            "username": "someone1",
            "password": "superpass2232",
            "email": "some@gmail.com",
        }
        with self.assertRaises(ValidationError) as e:
            self.client.post(reverse('login'), data=data, format='json')
            self.assertEqual("Such user does not exist", e.exception[0])

    def test_logout(self):
        response = self.client.post(
            reverse('login'), data=self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.token = RefreshToken.for_user(self.user)
        self.client.credentials(
            HTTP_AUTHORIZATION=f'Bearer {self.token.access_token}')
        response = self.client.post(reverse('logout'), format='json')
        self.assertEqual(response.status_code, status.HTTP_205_RESET_CONTENT)
