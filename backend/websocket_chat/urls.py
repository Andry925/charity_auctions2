from django.urls import path
from . import views

urlpatterns = [
    path(
        'start/',
        views.CreateConversation.as_view(),
        name='start_conversation'),
    path(
        '<int:pk>/',
        views.ConversationDetail.as_view(),
        name='detail_conversation'),
    path(
        '',
        views.ListConversations.as_view(),
        name='my_conversations')]
