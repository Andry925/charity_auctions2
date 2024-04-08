from django.urls import path
from . import views

urlpatterns = [
    path(
        'all_auctions/',
        views.AuctionListView.as_view(),
        name='all_auctions'),
    path(
        'particular_auction/<int:pk>/',
        views.AuctionOwnerDetailView.as_view(),
        name='manage_auction'),
    path(
        'my_auctions/',
        views.AuctionOwnerView.as_view(),
        name='my_auctions'
    ),
    path(
        "auction_detail/<int:pk>/",
        views.AuctionDetailView.as_view(),
        name='auction_detail'
    )]
