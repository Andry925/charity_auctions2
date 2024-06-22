from rest_framework import serializers
from .models import Conversation, Message


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['text']


class ConversationListSerializer(serializers.ModelSerializer):
    initiator = serializers.CharField()
    receiver = serializers.CharField()
    last_message = serializers.SerializerMethodField()

    class Meta:
        model = Conversation
        fields = ['initiator', 'receiver', 'last_message']

    def get_last_message(self, instance):
        message = instance.message_set.first()
        return MessageSerializer(instance=message)


class ConversationSerializer(serializers.ModelSerializer):
    initiator = serializers.StringRelatedField()
    receiver = serializers.StringRelatedField()
    message_set = MessageSerializer(many=True, required=False)

    class Meta:
        model = Conversation
        fields = '__all__'
