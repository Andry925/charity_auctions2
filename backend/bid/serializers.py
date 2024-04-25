from rest_framework import serializers
from .models import Bid


class BidSerializer(serializers.ModelSerializer):
    bidder = serializers.CharField(source='bidder.username', read_only=True)

    class Meta:
        model = Bid
        fields = '__all__'
