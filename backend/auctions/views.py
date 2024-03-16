from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import permissions
from rest_framework.authentication import TokenAuthentication
from rest_framework import generics
from .models import Auction
from .serializers import AuctionSerializer


class AuctionListView(generics.ListCreateAPIView):
    queryset = Auction.objects.all()
    serializer_class = AuctionSerializer
    parser_classes = [MultiPartParser, FormParser]
    permissions = [permissions.IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class AuctionDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Auction.objects.all()
    serializer_class = AuctionSerializer
    parser_classes = [MultiPartParser, FormParser]
    permissions = [permissions.IsAuthenticated]
    authentication_classes = [TokenAuthentication]
