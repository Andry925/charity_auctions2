from django.urls import path
from . import views

urlpatterns = [
    path(
        'new-bid/<int:pk>',
        views.BidCreateView.as_view(),
        name='manage_bids'),

    path(
        'all-bids/',
        views.ListBidView.as_view(),
        name='all_bids')


]
