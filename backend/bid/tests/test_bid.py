import json
from django.urls import reverse
from rest_framework import status
from .setup import TestBidAuctionSetup

EXTRA_KEYS = ("bid_date", "updated_at")


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
        error_message = json.loads(response.content)['non_field_errors'][0]

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(error_message, "Bid can not be less than start_price")

