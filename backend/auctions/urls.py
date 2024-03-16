from django.urls import path
from . import views

urlpatterns = [
    path(
        'all_auctions/',
        views.AuctionListView.as_view(),
        name='all_auctions'),
    path(
        'particular_auction/<int:pk>/',
        views.AuctionDetailView.as_view(),
        name='create_auction')]
