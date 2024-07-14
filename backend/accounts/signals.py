from django.core.mail import EmailMultiAlternatives
from django.dispatch import receiver
from django.template.loader import render_to_string
from django.urls import reverse
from .tasks import reset_password

from django_rest_passwordreset.signals import reset_password_token_created


@receiver(reset_password_token_created)
def password_reset_token_created(
        sender,
        instance,
        reset_password_token,
        *args,
        **kwargs):
    reset_password.delay(instance = str(instance), reset_password_token = str(reset_password_token))

