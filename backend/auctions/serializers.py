from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from bid.serializers import BidSerializer
from .models import Auction


class AuctionSerializer(serializers.ModelSerializer):
    bids_auction = BidSerializer(read_only=True, many=True)
    image_url = serializers.ImageField(required=False)
    user = serializers.ReadOnlyField(source='user.username')
    bids = serializers.ReadOnlyField(source='bids.bid_amount')

    class Meta:
        model = Auction
        fields = '__all__'

    def validate(self, validated_data):
        user = self.context['request'].user
        if Auction.objects.filter(user=user).count() > 3:
            raise ValidationError(
                "Sorry, but you can not have more than three auctions"
            )
        return validated_data


class AuctionPerUserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(read_only=True)
    total = serializers.IntegerField(read_only=True)

    class Meta:
        model = Auction
        fields = ('username', 'total')
