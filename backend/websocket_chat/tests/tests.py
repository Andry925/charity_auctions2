import json
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from django.contrib.auth import get_user_model
from websocket_chat.models import Conversation
from rest_framework_simplejwt.tokens import RefreshToken

EXTRA_KEYS = ("bid_date", "updated_at")

User = get_user_model()


class ConversationTests(APITestCase):

    def setUp(self):
        self.client = APIClient()
        user1_data = self.parse_test_config_file().get("user_credentials")
        user2_data = self.parse_test_config_file().get("second_user_credentials")
        self.user1 = User.objects.create_user(**user1_data)
        self.user2 = User.objects.create_user(**user2_data)
        self.token_first_user = RefreshToken.for_user(self.user1)
        self.token_second_user = RefreshToken.for_user(self.user2)

    def test_create_conversation_success(self):
        url = reverse('start_conversation')
        data = {'username': 'tester1232'}
        self.client.credentials(
            HTTP_AUTHORIZATION=f'Bearer {self.token_first_user.access_token}')
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Conversation.objects.count(), 1)
        self.assertEqual(Conversation.objects.first().initiator, self.user1)
        self.assertEqual(Conversation.objects.first().receiver, self.user2)

    def test_create_conversation_user_not_found(self):
        url = reverse('start_conversation')
        data = {'username': 'invalid_user'}
        self.client.credentials(
            HTTP_AUTHORIZATION=f'Bearer {self.token_first_user.access_token}')
        self.client.post(url, data, format='json')
        self.assertEqual(Conversation.objects.count(), 0)

    def test_create_conversation_already_exists(self):
        Conversation.objects.create(initiator=self.user1, receiver=self.user2)
        url = reverse('start_conversation')
        data = {'username': 'tester1232'}
        self.client.credentials(
            HTTP_AUTHORIZATION=f'Bearer {self.token_first_user.access_token}')
        self.client.post(url, data, format='json')
        self.assertEqual(Conversation.objects.count(), 1)

    def test_list_conversations(self):
        Conversation.objects.create(initiator=self.user1, receiver=self.user2)
        url = reverse('my_conversations')
        self.client.credentials(
            HTTP_AUTHORIZATION=f'Bearer {self.token_first_user.access_token}')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["initiator"], "tester123@gmail.com")
        self.assertEqual(response.data[0]["receiver"], "tester1232@gmail.com")

    def test_retrieve_conversation_detail(self):
        conversation = Conversation.objects.create(
            initiator=self.user1, receiver=self.user2)
        url = reverse('detail_conversation', kwargs={'pk': conversation.id})
        self.client.credentials(
            HTTP_AUTHORIZATION=f'Bearer {self.token_first_user.access_token}')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get("initiator"), 'tester123@gmail.com')
        self.assertEqual(response.data.get("receiver"), 'tester1232@gmail.com')

    @staticmethod
    def parse_test_config_file():
        with open("websocket_chat/tests/config.json", encoding='utf-8') as config_file:
            json_data = json.load(config_file)

        return json_data

    @staticmethod
    def remove_extra_keys_from_dict(dict_data):
        for key in EXTRA_KEYS:
            dict_data.pop(key, None)
        return dict_data
