from django.urls import reverse
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase
from rest_framework import status
from auctions.models import Auction
from .models import Bid
import json

EXTRA_KEYS = ("bid_date", "updated_at")


class TestBidAuctionSetup(APITestCase):

    def setUp(self) -> None:
        self.initial_cleaned_dict_data = self.parse_test_config_file()
        self.cleaned_dict_data = self.remove_extra_keys_from_dict(
            self.initial_cleaned_dict_data)
        print(self.cleaned_dict_data)
        self.first_user = get_user_model().objects.create_user(
            **self.cleaned_dict_data.get("user_credentials"))
        self.second_user = get_user_model().objects.create_user(
            **self.cleaned_dict_data.get("second_user_credentials"))
        self.cleaned_dict_data.get("auction_data")["user"] = self.first_user
        self.auction = Auction.objects.create(
            **self.cleaned_dict_data.get("auction_data"))
        self.cleaned_dict_data.get("bid_data")["bidder"] = self.second_user
        self.cleaned_dict_data.get("bid_data")["auction"] = self.auction
        self.bid = Bid.objects.create(**self.cleaned_dict_data.get("bid_data"))
        self.client.post(
            reverse('login'),
            data=self.cleaned_dict_data.get("user_credentials"),
            format='json')
        self.client.post(
            reverse('login'),
            data=self.cleaned_dict_data.get("second_user_credentials"),
            format='json')
        self.token_first_user = Token.objects.get(user__username='tester123')
        self.token_second_user = Token.objects.get(
            user__username='tester1232')

    def tearDown(self) -> None:
        self.client.logout()
        self.bid.delete()
        self.auction.delete()
        self.first_user.delete()
        self.second_user.delete()
        Token.objects.filter(user__username='testuser123').delete()
        Token.objects.filter(user__username='testuser1232').delete()

    @staticmethod
    def parse_test_config_file():
        with open("/home/andrew/PycharmProjects/charity_auctions2/new/charity_auctions2/backend/bid/config.json", encoding='utf-8') as config_file:
            json_data = json.load(config_file)

        return json_data

    @staticmethod
    def remove_extra_keys_from_dict(dict_data):
        for key in EXTRA_KEYS:
            dict_data.pop(key, None)
        return dict_data


class TestBidEndpoints(TestBidAuctionSetup):

    def test_bids_are_sent(self):
        self.client.credentials(
            HTTP_AUTHORIZATION='Token ' +
            self.token_first_user.key)
        response = self.client.get(reverse('all_bids'), format='json')
        response_data = response.content
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        cleaned_response = TestBidAuctionSetup.remove_extra_keys_from_dict(
            json.loads(response_data)[0])
        self.assertEqual(
            cleaned_response,
            {
                'id': 1,
                'bidder': 'tester1232@gmail.com',
                'auction': 'test description',
                'bid_amount': '15.00',
                'description': None})
