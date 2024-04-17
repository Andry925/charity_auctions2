from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import permissions, status
from rest_framework import filters
from rest_framework.authentication import TokenAuthentication
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination
from .models import Auction
from .serializers import AuctionSerializer, AuctionPerUserSerializer


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


class AuctionFilterView(generics.ListAPIView):
    search_fields = ["description", "user__username"]
    filter_backends = [filters.SearchFilter, ]
    queryset = Auction.objects.all()
    serializer_class = AuctionSerializer
    parser_classes = [MultiPartParser, FormParser]
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    pagination_class = AuctionCustomPaginator


class AuctionsPerUserView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    pagination_class = AuctionCustomPaginator

    def get(self, request):
        queryset = Auction.objects.raw(
            "SELECT 1 AS id, username, COUNT(*) as total "
            "FROM auctions_auction "
            "JOIN accounts_user ON auctions_auction.user_id = accounts_user.id "
            "GROUP BY username")
        serializer = AuctionPerUserSerializer(queryset, many=True)
        return Response(serializer.data, status.HTTP_200_OK)
