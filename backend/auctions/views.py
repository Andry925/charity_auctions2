from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import permissions
from rest_framework.authentication import TokenAuthentication
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from .models import Auction
from .serializers import AuctionSerializer


class AuctionCustomPaginator(PageNumberPagination):
    page_size = 5


class AuctionListView(generics.ListCreateAPIView):
    queryset = Auction.objects.all()
    serializer_class = AuctionSerializer
    parser_classes = [MultiPartParser, FormParser]
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    pagination_class = AuctionCustomPaginator

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class AuctionDetailView(generics.RetrieveAPIView):
    queryset = Auction.objects.all()
    serializer_class = AuctionSerializer
    parser_classes = [MultiPartParser, FormParser]
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [TokenAuthentication]


class AuctionOwnerDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AuctionSerializer
    parser_classes = [MultiPartParser, FormParser]
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def get_queryset(self):
        current_user = self.request.user
        return Auction.objects.filter(user=current_user)


class AuctionOwnerView(generics.ListAPIView):
    serializer_class = AuctionSerializer
    parser_classes = [MultiPartParser, FormParser]
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    pagination_class = AuctionCustomPaginator

    def get_queryset(self):
        current_user = self.request.user
        return Auction.objects.filter(user=current_user)
