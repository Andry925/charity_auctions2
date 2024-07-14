from django.urls import path
from . import views

urlpatterns = [
    path(
        'all-auctions',
        views.AuctionListView.as_view(),
        name='all_auctions'),
    path(
        'my-auction/<int:pk>',
        views.AuctionOwnerDetailView.as_view(),
        name='manage_auction'),
    path(
        'my-auctions',
        views.AuctionOwnerView.as_view(),
        name='my_auctions'
    ),
    path(
        "auction-detail/<int:pk>",
        views.AuctionDetailView.as_view(),
        name='auction_detail'
    ),
    path(
        "auctions-per-user",
        views.AuctionsPerUserView.as_view(),
        name='auctions_per_user'
    ),
    path(
        "filter-auctions",
        views.AuctionFilterView.as_view(),
        name='filter_auction'
    ),
]
