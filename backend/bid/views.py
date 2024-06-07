from django.shortcuts import get_object_or_404
from rest_framework.exceptions import PermissionDenied
from rest_framework.authentication import TokenAuthentication
from rest_framework import permissions, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from auctions.models import Auction
from .models import Bid
from .serializers import BidSerializer


class BidCreateView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        auction_model = self.validate_auction_bid(request=request, pk=pk)
        bid_serializer = BidSerializer(
            data=request.data, context={
                'auction_model': auction_model})
        if bid_serializer.is_valid(raise_exception=True):
            model_object = bid_serializer.save(bidder=request.user)
            model_object.auction = auction_model
            auction_model.current_bid = model_object.bid_amount
            model_object.save()
            auction_model.save()

            return Response(
                bid_serializer.data,
                status=status.HTTP_201_CREATED)

    def validate_auction_bid(self, request, pk):
        auction = get_object_or_404(Auction, pk=pk)
        if auction.user == request.user:
            raise ValueError("You can not bid your own auctions")
        return auction


class BidListView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        auctions = Bid.objects.all().select_related("bidder", "auction")
        serializer = BidSerializer(auctions, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
