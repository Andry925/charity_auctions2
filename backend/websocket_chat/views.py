from django.db.models import Q
from django.contrib.auth import get_user_model
from rest_framework import generics, status
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
        if isinstance(participant, Response):
            return participant
        conversation = Conversation.objects.filter(
            Q(
                initiator=self.request.user,
                receiver=participant) | Q(
                initiator=participant,
                receiver=self.request.user)).select_related(
            "initiator",
            "receiver")
        if conversation.exists():
            return Response({"message":"This conversation already exists"})

        serializer.save(initiator=self.request.user, receiver=participant)

    def get_conversation_participant(self, request):
        participant_username = request.data.get('username')
        try:
            participant = user_model.objects.get(username=participant_username)

        except user_model.DoesNotExist:
            return Response({'error': 'User not found'})
        return participant


class UserConversationQueryset:

    def get_queryset(self):
        queryset = Conversation.objects.filter(
            Q(initiator=self.request.user) | Q(receiver=self.request.user)
        ).select_related("initiator", "receiver")
        return queryset


class ListConversations(UserConversationQueryset, generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ConversationListSerializer


class ConversationDetail(UserConversationQueryset, generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ConversationSerializer
