from django.db import models
from django.conf import settings


class Conversation(models.Model):
    initiator = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        related_name='conv_initiator')
    receiver = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        related_name='conv_reciever')
    start_time = models.DateTimeField(auto_now_add=True)


class Message(models.Model):
    sender = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        related_name='message_sender')
    conversation = models.ForeignKey(
        Conversation,
        on_delete=models.SET_NULL,
        related_name='conversation_messages')
    text = models.TextField(max_length=1024, null=True, blank=True)
    attached_file = models.FileField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created_at',)
