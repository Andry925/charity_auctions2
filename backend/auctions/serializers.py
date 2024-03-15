from rest_framework import serializers
from .models import Auction


class AuctionSerializer(serializers.ModelSerializer):
    image_url = serializers.ImageField(required=False)
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Auction
        fields = '__all__'
