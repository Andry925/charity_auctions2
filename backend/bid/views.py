from django.shortcuts import get_object_or_404
from rest_framework.exceptions import PermissionDenied
from rest_framework.authentication import TokenAuthentication
from rest_framework import permissions, status
from rest_framework.views import APIView
from rest_framework.response import Response
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
            auction_model.bids = model_object
            auction_model.save()

            return Response(
                bid_serializer.data,
                status=status.HTTP_201_CREATED)

    def validate_auction_bid(self, request, pk):
        auction = get_object_or_404(Auction, pk=pk)
        if auction.user == request.user:
            raise PermissionDenied("You can not bid your own auctions")
        return auction


class BidListView(APIView):
    def get(self, request):
        auctions = Bid.objects.all()
        serializer = BidSerializer(auctions, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
