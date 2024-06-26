from rest_framework import serializers
from .models import Bid


class BidSerializer(serializers.ModelSerializer):
    bidder = serializers.CharField(read_only=True)
    auction = serializers.CharField(read_only=True)

    class Meta:
        model = Bid
        fields = [
            "bidder",
            "bid_amount",
            "auction",
            "bid_date",
            "updated_at",
            "description"]

    def validate(self, validated_data):
        start_price = float(self.context.get('bidded_auction').starting_price)
        current_bid = float(self.context.get('bidded_auction').current_bid)
        offered_bid = float(validated_data.get('bid_amount'))

        if offered_bid and start_price >= offered_bid:
            raise serializers.ValidationError(
                'Bid can not be less than start_price')
        elif current_bid and current_bid >= offered_bid:
            raise serializers.ValidationError(
                'Offered bid can not be less than current_bid')
        return validated_data
