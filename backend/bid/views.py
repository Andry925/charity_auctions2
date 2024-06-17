from django.shortcuts import get_object_or_404
from rest_framework import permissions
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from auctions.models import Auction
from .models import Bid
from .serializers import BidSerializer


class BidCustomPaginator(PageNumberPagination):
    page_size = 5


class BidCreateView(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = BidSerializer
    pagination_class = BidCustomPaginator

    def perform_create(self, serializer):
        bidded_auction = self.validated_auction_bid(
            request=self.request, pk=self.kwargs["pk"])
        serializer.save(bidder=self.request.user, auction=bidded_auction)
        bidded_auction.current_bid = serializer.validated_data["bid_amount"]
        bidded_auction.save()

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context.update({"bidded_auction": self.validated_auction_bid(
            request=self.request, pk=self.kwargs["pk"])})
        return context

    def validated_auction_bid(self, request, pk):
        auction = get_object_or_404(Auction, pk=pk)
        if auction.user == request.user:
            raise ValueError("You can not bid your own auctions")
        return auction


class ListBidView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = BidSerializer
    pagination_class = BidCustomPaginator

    def get_queryset(self):
        queryset = Bid.objects.filter(
            bidder=self.request.user).select_related(
            "bidder", "auction")
        return queryset

