from rest_framework import serializers
from .models import Conversation, Message


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['text']


class ConversationListSerializer(serializers.ModelSerializer):
    initiator = serializers.CharField()
    receiver = serializers.CharField()

    class Meta:
        model = Conversation
        fields = ['initiator', 'receiver']


class ConversationSerializer(serializers.ModelSerializer):
    initiator = serializers.StringRelatedField()
    receiver = serializers.StringRelatedField()
    message_set = MessageSerializer(many=True, required=False)

    class Meta:
        model = Conversation
        fields = '__all__'
