import json
from django.urls import reverse
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.test import APITestCase
from auctions.models import Auction
from bid.models import Bid

EXTRA_KEYS = ("bid_date", "updated_at")


class TestBidAuctionSetup(APITestCase):

    def setUp(self) -> None:
        self.initial_cleaned_dict_data = self.parse_test_config_file()
        self.cleaned_dict_data = self.remove_extra_keys_from_dict(
            self.initial_cleaned_dict_data)
        self.create_users()
        self.create_auction_and_bid()
        self.authenticate_users()

    def tearDown(self) -> None:
        self.client.logout()
        self.bid.delete()
        self.auction.delete()
        self.first_user.delete()
        self.second_user.delete()


    def create_users(self):
        self.first_user = get_user_model().objects.create_user(
            **self.cleaned_dict_data.get("user_credentials"))
        self.second_user = get_user_model().objects.create_user(
            **self.cleaned_dict_data.get("second_user_credentials"))

    def create_auction_and_bid(self):
        self.cleaned_dict_data.get("auction_data")["user"] = self.first_user
        self.auction = Auction.objects.create(
            **self.cleaned_dict_data.get("auction_data"))
        self.cleaned_dict_data.get("bid_data")["bidder"] = self.second_user
        self.cleaned_dict_data.get("bid_data")["auction"] = self.auction
        self.bid = Bid.objects.create(**self.cleaned_dict_data.get("bid_data"))

    def authenticate_users(self):
        self.client.post(
            reverse('login'),
            data=self.cleaned_dict_data.get("user_credentials"),
            format='json')
        self.client.post(
            reverse('login'),
            data=self.cleaned_dict_data.get("second_user_credentials"),
            format='json')
        self.token_first_user = RefreshToken.for_user(self.first_user)
        self.token_second_user = RefreshToken.for_user(self.second_user)


    @staticmethod
    def parse_test_config_file():
        with open("bid/config.json", encoding='utf-8') as config_file:
            json_data = json.load(config_file)

        return json_data

    @staticmethod
    def remove_extra_keys_from_dict(dict_data):
        for key in EXTRA_KEYS:
            dict_data.pop(key, None)
        return dict_data
