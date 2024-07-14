from django.urls import path
from . import views

urlpatterns = [
    path(
        'new-conversation',
        views.CreateConversation.as_view(),
        name='start_conversation'),
    path(
        'particular-conversation/<int:pk>',
        views.ConversationDetail.as_view(),
        name='detail_conversation'),
    path(
        'my-conversations',
        views.ListConversations.as_view(),
        name='my_conversations')]
