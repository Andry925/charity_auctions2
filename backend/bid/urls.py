from django.urls import path
from . import views

urlpatterns = [
    path(
        'create_bid/<int:pk>/',
        views.BidCreateView.as_view(),
        name='manage_bids'),

    path(
        'all_bids/',
        views.BidListView.as_view(),
        name='all_bids')]


]

