from django.shortcuts import  redirect, reverse
from django.db.models import Q
from django.contrib.auth import get_user_model
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import permissions
from .serializers import ConversationListSerializer, ConversationSerializer
from .models import Conversation


user_model = get_user_model()


class CreateConversation(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ConversationSerializer

    def perform_create(self, serializer):
        participant = self.get_conversation_participant(
            request=self.request)
        conversation = Conversation.objects.filter(
            Q(
                initiator=self.request.user,
                receiver=participant) | Q(
                initiator=participant,
                receiver=self.request.user))
        if conversation.exists():
            return redirect(
                reverse(
                    'detail_conversation',
                    args=(
                        conversation[0].id,
                    )))

        serializer.save(initiator=self.request.user, receiver=participant)

    def get_conversation_participant(self, request):
        participant_username = request.data.get('username')
        try:
            participant = user_model.objects.get(username=participant_username)

        except user_model.DoesNotExist:
            return Response({'error': 'User not found'})
        return participant


class ListConversations(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ConversationListSerializer

    def get_queryset(self):
        queryset = Conversation.objects.filter(
            Q(initiator=self.request.user) | Q(receiver=self.request.user))
        return queryset


class ConversationDetail(generics.RetrieveAPIView):
    queryset = Conversation.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ConversationSerializer
