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
        self.create_users()
        self.create_auction_and_bid()
        self.authenticate_users()

    def tearDown(self) -> None:
        self.client.logout()
        self.bid.delete()
        self.auction.delete()
        self.first_user.delete()
        self.second_user.delete()
        Token.objects.filter(user__username='testuser123').delete()
        Token.objects.filter(user__username='testuser1232').delete()

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
        self.token_first_user = Token.objects.get(user__username='tester123')
        self.token_second_user = Token.objects.get(
            user__username='tester1232')

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
                'bidder': 'tester1232@gmail.com',
                'auction': 'test description',
                'bid_amount': '15.00',
                'description': None})

    def test_bid_is_created(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token_second_user.key)
        self.cleaned_dict_data.get("bid_data")["bid_amount"] = 20
        response = self.client.post(reverse('manage_bids', args=[self.auction.id]), data=self.cleaned_dict_data.get("bid_data"))
        current_price = float(json.loads(response.content)["bid_amount"])
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(current_price, 20.00)

    def test_try_bid_own_auction(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token_first_user.key)
        self.cleaned_dict_data.get("bid_data")["bid_amount"] = 20
        with self.assertRaises(ValueError) as e:
            self.client.post(reverse('manage_bids', args=[self.auction.id]),
                                    data=self.cleaned_dict_data.get("bid_data"))
        self.assertEqual("You can not bid your own auctions", e.exception.args[0])


    def test_try_bid_less_price(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token_second_user.key)
        self.cleaned_dict_data.get("bid_data")["bid_amount"] = 10
        response = self.client.post(reverse('manage_bids', args=[self.auction.id]),
                                    data=self.cleaned_dict_data.get("bid_data"))
        current_price = float(json.loads(response.content)["bid_amount"])
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(current_price, 20.00)
